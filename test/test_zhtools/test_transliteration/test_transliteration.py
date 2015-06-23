from zhtools.transliteration import Transliteration
import unittest


class TestTransliteration(unittest.TestCase):

    def test_split_syllables(self):
        self.assertEqual(Transliteration("wo3bu4zhi1dao4").text,
                        ["wo3","bu4","zhi1","dao4"])
        self.assertEqual(Transliteration("zhe4r").text, ["zhe4","r"])
        self.assertEqual(Transliteration("san1 C").text, ["san1","C"])
        self.assertEqual(Transliteration("A B zhi1").text, ["A","B","zhi1"])

    def test_pinyin(self):
        self.assertEqual(Transliteration("zhe4r").get_pinyin(), "zhèr")
        self.assertEqual(Transliteration("lu:e4").get_pinyin(), "lüè")
        self.assertEqual(Transliteration("yi1hui4r5").get_pinyin(), "yīhuìr")

    def test_pinyin_capitals(self):
        self.assertEqual(Transliteration("Mao2 Ze2 dong1").get_pinyin(),
                         "Máo Zédōng")
        self.assertEqual(Transliteration("A B zhi1").get_pinyin(), "A B zhī")

    def test_non_implemented_tranlisteration(self):
        with self.assertRaises(AttributeError):
            Transliteration("").get_non_existing_transliteration_method()

    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            Transliteration("").nonono()

    def test_comma_is_excluded(self):
        expected = ["zhi4", "zhe3", "qian1", "lü4", ",",
                    "bi4", "you3", "yi1", "shi1"]
        self.assertEqual(Transliteration("".join(expected)).text, expected)
