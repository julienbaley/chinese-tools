from zhtools.transliteration.bopomofo import Bopomofo
import unittest


class TestPinyin(unittest.TestCase):
    def test_bopomofo(self):
        test_cases = [('a', 'ㄚ'), ('o', 'ㄛ'), ('e', 'ㄜ'), ('ai', 'ㄞ'),
                      ('ao', 'ㄠ'), ('ou', 'ㄡ'), ('an', 'ㄢ'), ('en', 'ㄣ'),
                      ('ang', 'ㄤ'), ('eng', 'ㄥ'), ('er', 'ㄦ'), ('yi', 'ㄧ'),
                      ('ye', 'ㄧㄝ'), ('you', 'ㄧㄡ'), ('yan', 'ㄧㄢ'),
                      ('yin', 'ㄧㄣ'), ('ying', 'ㄧㄥ'), ('wu', 'ㄨ'),
                      ('wo', 'ㄨㄛ'), ('wei', 'ㄨㄟ'), ('wen', 'ㄨㄣ'),
                      ('weng', 'ㄨㄥ'), ('ong', 'ㄨㄥ'), ('yu', 'ㄩ'),
                      ('yue', 'ㄩㄝ'), ('yuan', 'ㄩㄢ'), ('yun', 'ㄩㄣ'),
                      ('yong', 'ㄩㄥ'), ('bo', 'ㄅㄛ'), ('po', 'ㄆㄛ'),
                      ('mo', 'ㄇㄛ'), ('feng', 'ㄈㄥ'), ('diu', 'ㄉㄧㄡ'),
                      ('dui', 'ㄉㄨㄟ'), ('dun', 'ㄉㄨㄣ'), ('te', 'ㄊㄜ'),
                      ('nü', 'ㄋㄩ'), ('lü', 'ㄌㄩ'), ('ger', 'ㄍㄜㄦ'),
                      ('ke', 'ㄎㄜ'), ('he', 'ㄏㄜ'), ('jian', 'ㄐㄧㄢ'),
                      ('jiong', 'ㄐㄩㄥ'), ('qin', 'ㄑㄧㄣ'), ('xuan', 'ㄒㄩㄢ'),
                      ('zhe', 'ㄓㄜ'), ('zhi', 'ㄓ'), ('che', 'ㄔㄜ'),
                      ('chi', 'ㄔ'), ('she', 'ㄕㄜ'), ('shi', 'ㄕ'),
                      ('re', 'ㄖㄜ'), ('ri', 'ㄖ'), ('ze', 'ㄗㄜ'),
                      ('zuo', 'ㄗㄨㄛ'), ('zi', 'ㄗ'), ('ce', 'ㄘㄜ'),
                      ('ci', 'ㄘ'), ('se', 'ㄙㄜ'), ('si', 'ㄙ')]

        for py, bpmf in test_cases:
            self.assertEqual(Bopomofo(py + "1").syl, bpmf)
