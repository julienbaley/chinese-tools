import zhtools.transliteration.pinyin as py
import unittest

class TestPinyin(unittest.TestCase):
    
    def test_find_marked_vowel(self):
        self.assertEqual(py.find_marked_vowel("chuang"), "a")
        self.assertEqual(py.find_marked_vowel("duo"), "o")
        self.assertEqual(py.find_marked_vowel("lüe"), "e")
        self.assertEqual(py.find_marked_vowel("dao"), "a")
        self.assertEqual(py.find_marked_vowel("mou"), "o")
        self.assertEqual(py.find_marked_vowel("qie"), "e")
    
    def test_tone_number_to_mark(self):
        self.assertEqual(py.tone_number_to_mark("wo3bu4zhi1dao4"), "wǒbùzhīdào")
        self.assertEqual(py.tone_number_to_mark("zhe4r"), "zhèr")
        with self.assertRaises(Exception):
            py.tone_number_to_mark("zhe")
