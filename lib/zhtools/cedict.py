import os
import re
from collections import defaultdict
from .transliteration import Transliteration
from .transliteration.colour import copy_colour, minimize_colour


class Entry:
    def __init__(self, idx, trad, simp, pinyin, defs):
        self.idx = idx
        self.trad = trad
        self.simp = simp
        self.pinyin = pinyin
        self.defs = defs

    def realize(self, colour=False):
        self.pinyin = Transliteration(self.pinyin).get_pinyin(colour)
        if colour:
            self.trad = minimize_colour(copy_colour(self.pinyin, self.trad))
            self.simp = minimize_colour(copy_colour(self.pinyin, self.simp))
        self.pinyin = minimize_colour(self.pinyin)

    def __str__(self):
        return "{idx}\n{trad}\n{simp}\n{pinyin}\n{defs}"\
            .format(idx=self.idx,
                    trad=self.trad,
                    simp=self.simp,
                    pinyin=self.pinyin,
                    defs=self.defs)


class CEdict:

    def __init__(self,
                 filename=os.path.join("data", "cedict.txt"),
                 colour=False):
        self.parse_dict(filename)
        self.colour = colour

    def parse_dict(self, filename):
        # line format: trad simp [pin1 yin1] /def1/def2/.../defn/
        regex = "^(?P<trad>\S+) (?P<simp>\S+) \[(?P<pinyin>.*?)\] "\
                + "/(?P<defs>.*)/$"
        parse_regex = re.compile(regex)
        self.dict = defaultdict(list)

        with open(filename) as f:
            for idx, line in enumerate(f):
                if not line.startswith("#"):
                    e = Entry(idx, **parse_regex.match(line).groupdict())
                    self.dict[e.trad].append(e)
                    if e.simp != e.trad:
                        self.dict[e.simp].append(e)

    def __getitem__(self, key):
        if key not in self.dict:
            raise KeyError(key)
        es = self.dict[key]
        for e in es:
            e.realize(self.colour)
        return es
