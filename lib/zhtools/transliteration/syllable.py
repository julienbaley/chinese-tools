import re
from . import colour

class Syllable:    
    format = "[a-zA-Zü]{1,6}[1-5]?"
    
    def __init__(self, syllable):
        self.syl = syllable
        self.tone = 0
        self.phones = str()
        self.parse()
    
    def is_valid(self):
        if not hasattr(self, "valid"):
            self.valid = bool(re.match("^" + Syllable.format + "$", self.syl))
        return self.valid
    
    def parse(self):
        if self.is_valid():
            try:
                self.tone = int(self.syl[-1])
            except ValueError:
                pass
            else:
                self.phones = self.syl[:-1]
    
    def get_colour(self):
        return colour.apply_colour(self.syl, self.tone)
    
    def can_merge_left(self):
        return not self.syl.istitle()
    
    def can_merge_right(self):
        return len(self.syl) > 1 or not self.syl.istitle()
    
    def __str__(self): return self.syl
