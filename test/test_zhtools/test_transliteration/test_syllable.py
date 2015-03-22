from zhtools.transliteration.syllable import Syllable
import re
import unittest

class TestSyllable(unittest.TestCase):
    
    def test_empty_syllable(self):
        s = Syllable("")
        self.assertEqual(s.syl, "")
        self.assertEqual(s.tone, 0)
        self.assertEqual(s.phones, "")
    
    def test_invalid_syllable(self):
        s = Syllable("cr")
        self.assertEqual(s.syl, "cr")
        self.assertEqual(s.tone, 0)
        self.assertEqual(s.phones, "")
    
    def test_valid_syllable(self):
        s = Syllable("can1")
        self.assertEqual(s.syl, "can1")
        self.assertEqual(s.tone, 1)
        self.assertEqual(s.phones, "can")
    
    def test_color_is_only_html_marking(self):
        s = Syllable("can1")
        self.assertEqual(re.sub("<[^>]*>", "", s.get_color()), s.syl)
