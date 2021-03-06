import re
from .syllable import Syllable
from importlib import import_module


class Transliteration:

    def __init__(self, text):
        self.text = Transliteration.split_syllables(text.replace("u:", "ü"))

    @staticmethod
    def split_syllables(s):
        """Split along syllables but keep the rest"""
        return [syl.strip()
                for syl in re.split("("+Syllable.format+")", s)
                if len(syl.strip()) > 0]

    def __getattr__(self, name):
        # get_pinyin will use pinyin.Pinyin,
        # get_bopomofo will use bopomofo.Bopomofo etc
        if name.startswith("get_"):
            translit_method = name[len("get_"):]

            # we import the corresponding class
            try:
                module = import_module(".{mod}".format(mod=translit_method),
                                       __name__)
            except ImportError:
                msg = "'Transliteration' object has no attribute '{name}'"\
                    .format(name=name)
                raise AttributeError(msg)
            TransClass = getattr(module, translit_method.title())

            def get_translit(colour=False):
                merge_list = list()
                for syl in self.text:
                    tr = TransClass(syl)
                    syl = ("" if tr.can_merge_left() else " ")\
                        + (tr.get_colour() if colour else tr.syl)\
                        + ("" if tr.can_merge_right() else " ")
                    merge_list.append(syl)
                return re.sub("[ ]+", " ", "".join(merge_list)).strip()

            return get_translit
        else:
            msg = "'Transliteration' object has no attribute '{name}'"\
                  .format(name=name)
            raise AttributeError(msg)
