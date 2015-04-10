import re
from .syllable import Syllable

class Pinyin(Syllable):
    def __init__(self, syllable):
        Syllable.__init__(self, syllable)
        self.to_pinyin()
    
    tone_marks = { "a":"āáǎà",
                   "e":"ēéěè",
                   "i":"īíǐì",
                   "o":"ōóǒò",
                   "u":"ūúǔù",
                   "ü":"ǖǘǚǜ"}
    
    @staticmethod
    def find_marked_vowel(syllable):
        """Returns the vowel of the syllable that should receive the tone mark.
        
        Rules for tone mark placement can be found at http://www.pinyin.info/rules/where.html
        1. 'a' has priority over all
        2. 'e' comes right after
        3. 'o' receives the mark in ou (not in uo)
        4. in all other cases (which involve glides /w/, /ɥ/ and /j/), the last vowel takes the mark"""
        
        if "a" in syllable:
            return "a"
        elif "A" in syllable:
            return "A"
        elif "e" in syllable:
            return "e"
        elif "E" in syllable:
            return "E"
        elif "ou" in syllable:
            return "o"
        elif "Ou" in syllable:
            return "O"
        else:
            return re.search("(?P<last_vowel>[aeiouü])[^aeiouü]*$", syllable, re.IGNORECASE).group("last_vowel")
    
    def to_pinyin(self):
        if len(self.phones) > 0:
            if self.phones == "m":
                if self.tone == 2:
                    self.syl = "ḿ"
                elif self.tone == 4:
                    self.syl = "m`"
            else:
                v = Pinyin.find_marked_vowel(self.phones)
                replacement = Pinyin.tone_marks[v.lower()][self.tone-1] if 0 < self.tone < 5 else v #tone 5 is unmarked
                self.syl = self.phones.replace(v, replacement if v.islower() else replacement.upper())
