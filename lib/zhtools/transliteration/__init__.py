import re
from .syllable import Syllable
from .pinyin import Pinyin

from importlib import import_module

class Transliteration:
    
    def __init__(self, text):
        self.text = Transliteration.split_syllables(text.replace("u:","ü"))
    
    def split_syllables(s):
        return re.findall(Syllable.format, s)
    
    def __getattr__(self, name):
        #get_pinyin will use pinyin.Pinyin, get_bopomofo will use bopomofo.Bopomofo etc
        if name.startswith("get_"):
            translit_method = name[len("get_"):]
            
            #we import the corresponding class
            try:
                module = import_module(".{mod}".format(mod=translit_method), __name__)
            except ImportError:
                raise AttributeError("'Transliteration' object has no attribute '{name}'".format(name=name))
            TransClass = getattr(module, translit_method.title())
            
            def get_translit():
                merge_list = list()
                for syl in self.text:
                    tr = TransClass(syl)
                    syl = ("" if tr.can_merge_left() else " ") + tr.syl + ("" if tr.can_merge_right() else " ")
                    merge_list.append(syl)
                return re.sub("[ ]+", " ", "".join(merge_list)).strip()
                
            return get_translit
        else:
            raise AttributeError("'Transliteration' object has no attribute '{name}'".format(name=name))
