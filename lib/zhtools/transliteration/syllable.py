import re

class Syllable:
    format = "[a-zA-Zü]{1,6}[1-5]?"
    
    colour_coding = {   1 : "008000", #"green",
                        2 : "0000FF", #"blue",
                        3 : "800080", #"purple",
                        4 : "FF0000", #"red",
                        5 : "000000"} #"black"
    
    def __init__(self, syllable):
        self.syl = syllable
        self.tone = 0
        self.phones = str()
        self.parse()
    
    def is_valid(self):
        return re.match("^" + Syllable.format + "$", self.syl)
    
    def parse(self):
        if self.is_valid():
            try:
                self.tone = int(self.syl[-1])
            except ValueError:
                pass
            else:
                self.phones = self.syl[:-1]
    
    def get_color(self):
        return '<span style="color:#{col}">{syl}</span>'.format(col=Syllable.colour_coding[self.tone], syl=self.syl)
    
    def __str__(self): return self.syl
