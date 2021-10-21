import unittest
from machinetranslation.translator import english_to_french,french_to_english

class TestEgnlishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNone(None,english_to_french(""))
        self.assertEqual("Bonjour",english_to_french("Hello"))



class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(None,french_to_english(""))
        self.assertEqual("Hello",french_to_english("Bonjour"))


unittest.main()