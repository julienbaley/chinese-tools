from zhtools.transliteration import colour
import unittest

class TestColour(unittest.TestCase):
    
    def test_apply_and_strip_colour(self):
        s = "some string"
        self.assertEqual(colour.strip_colour(colour.apply_colour(s,0),0), s)
        self.assertNotEqual(colour.apply_colour(s,1), colour.apply_colour(s,2))
    
    def test_strip_all_colours(self):
        s = "abc"
        coloured_s = "".join([colour.apply_colour(c,i) for i, c in enumerate(s)])
        self.assertEqual(colour.strip_colour(coloured_s), s)
    
    def test_copy_colour_applies_the_colours_from_a_string_to_another(self):
        s = "abc"
        t = "@$*"
        coloured_s = "".join([colour.apply_colour(c,i) for i, c in enumerate(s)])
        coloured_t = colour.copy_colour(coloured_s, t)
        self.assertEqual(coloured_t.replace("@","a").replace("$","b").replace("*","c"), coloured_s)
    
    def test_minimize_colour(self):
        #same colour thrice
        s = """<span style="color:#0000FF">Lián</span><span style="color:#0000FF">hé</span><span style="color:#0000FF">guó</span>"""
        self.assertEqual(colour.minimize_colour(s), """<span style="color:#0000FF">Liánhéguó</span>""")
        
        #has some black
        s = """<span style="color:#0000FF">Lián</span><span style="color:#0000FF">hé</span><span style="color:#000000">guo</span>"""
        self.assertEqual(colour.minimize_colour(s), """<span style="color:#0000FF">Liánhé</span>guo""")
