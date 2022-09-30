import unittest
from machinetranslation.translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('accueillir'), 'welcome')
        self.assertNotEqual(french_to_english("aimer"), 'love')
        self.assertNotEqual(french_to_english("None"), '')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('welcome'), 'accueillir')
        self.assertNotEqual(english_to_french("love"), 'aimer')
        self.assertNotEqual(english_to_french("None"), '')


if __name__ == '__main__':
    unittest.main()