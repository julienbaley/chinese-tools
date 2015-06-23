from zhtools.transliteration.pinyin import Pinyin
import unittest


class TestPinyin(unittest.TestCase):

    def test_find_marked_vowel(self):
        self.assertEqual(Pinyin.find_marked_vowel("chuang"), "a")
        self.assertEqual(Pinyin.find_marked_vowel("duo"), "o")
        self.assertEqual(Pinyin.find_marked_vowel("lüe"), "e")
        self.assertEqual(Pinyin.find_marked_vowel("dao"), "a")
        self.assertEqual(Pinyin.find_marked_vowel("mou"), "o")
        self.assertEqual(Pinyin.find_marked_vowel("qie"), "e")
        self.assertEqual(Pinyin.find_marked_vowel("Er4"), "E")
        self.assertEqual(Pinyin.find_marked_vowel("Jing4"), "i")
        self.assertEqual(Pinyin.find_marked_vowel("Ao4"), "A")
        self.assertEqual(Pinyin.find_marked_vowel("Ou1"), "O")

    def test_normal_syllable(self):
        p = Pinyin("can1")
        self.assertEqual(p.syl, "cān")

    def test_light_tone(self):
        p = Pinyin("mo5")
        self.assertEqual(p.syl, "mo")

    def test_no_tone(self):
        p = Pinyin("mo")
        self.assertEqual(p.syl, "mo")

    def test_handles_special_case_m(self):
        p = Pinyin("m2")
        self.assertEqual(p.syl, "ḿ")
        p = Pinyin("m4")
        self.assertEqual(p.syl, "m`")

    def test_untoned_pinyin_is_left_as_is(self):
        p = Pinyin("can")
        self.assertEqual(p.syl, "can")
