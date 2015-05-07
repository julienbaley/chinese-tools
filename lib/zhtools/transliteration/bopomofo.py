import re
from .syllable import Syllable


class Bopomofo(Syllable):

    def __init__(self, syllable):
        Syllable.__init__(self, syllable)
        self.to_bopomofo()

    initials = {'b': 'ㄅ',
                'p': 'ㄆ',
                'm': 'ㄇ',
                'f': 'ㄈ',
                'd': 'ㄉ',
                't': 'ㄊ',
                'n': 'ㄋ',
                'l': 'ㄌ',
                'g': 'ㄍ',
                'k': 'ㄎ',
                'h': 'ㄏ',
                'j': 'ㄐ',
                'q': 'ㄑ',
                'x': 'ㄒ',
                'zh': 'ㄓ',
                'ch': 'ㄔ',
                'sh': 'ㄕ',
                'r': 'ㄖ',
                'z': 'ㄗ',
                'c': 'ㄘ',
                's': 'ㄙ'}

    finals = {'a':  'ㄚ',
              'o':  'ㄛ',
              'e':  'ㄜ',
              'ê':  'ㄝ',
              'ai': 'ㄞ',
              'ei': 'ㄟ',
              'ao': 'ㄠ',
              'ou': 'ㄡ',
              'an': 'ㄢ',
              'en': 'ㄣ',
              'ang': 'ㄤ',
              'eng': 'ㄥ',
              'er': 'ㄦ',
              'i':  'ㄧ',  # also n'i'ao /j/
              'u':  'ㄨ',  # also h'u'ang /w/
              'ü':  'ㄩ',  # also n'ü'e /
              'ï':  ''}  # zhi,chi,shi,ri,zi,ci,si are written without vowel

    tone_marks = {1: '', 2: 'ˊ', 3: 'ˇ', 4: 'ˋ', 5: '˙'}

    def to_bopomofo(self):
        if len(self.phones) > 0:
            # find initial
            syl = self.phones
            syl = re.sub("(j|q|x)u", r"\1ü", syl)
            syl = re.sub("(ch?|sh?|zh?|r)i", r"\1ï", syl)

            if syl[:2] in Bopomofo.initials:
                initial = syl[:2]
            elif syl[0] in Bopomofo.initials:
                initial = syl[0]
            else:
                initial = ''
            rest = syl[len(initial):]

            # find medial
            rest = rest.replace("iu", "iou")    \
                       .replace("ui", "uei")    \
                       .replace("wu", "u")      \
                       .replace("yi", "i")      \
                       .replace("yu", "ü")      \
                       .replace("yong", "üeng") \
                       .replace("iong", "üeng") \
                       .replace("ong", "ueng")

            if rest.startswith('ü') and len(rest) > 1:
                medial = 'ü'
            elif rest.startswith('y') or (rest.startswith('i') and len(rest)):
                medial = 'i'
            elif rest.startswith('w') or (rest.startswith('u') and len(rest)):
                medial = 'u'
            else:
                medial = ''
            rest = rest[len(medial):]

            # find final
            erhua = ''
            if rest == 'e' and medial in ('i', 'ü'):
                final = 'ê'
            elif rest == 'n':
                final = 'en'
            elif rest == 'ng':
                final = 'eng'
            elif rest == 'er' and len(initial) > 0:
                final = 'e'
                erhua = 'er'
            else:
                final = rest

            self.syl = ''.join([Bopomofo.initials.get(initial, ''),
                                Bopomofo.finals.get(medial, ''),
                                Bopomofo.finals.get(final, ''),
                                Bopomofo.finals.get(erhua, ''),
                                Bopomofo.tone_marks.get(self.tone, '')])
