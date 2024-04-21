import unittest
from profanitypy.client import ProfanityApi


class TestProfanityAPI(unittest.TestCase):
    def setUp(self):
        # Initialize the ProfanityAPI instance
        self.api = ProfanityApi()

    def test_check_profanity(self):
        result = self.api.check_profanity("sex")
        self.assertTrue(result.profanity)
        self.assertEqual(result.score, 0.9205664)

    def test_no_profanity(self):
        result = self.api.check_profanity("This message is clean.")
        self.assertFalse(result.profanity)
        self.assertEqual(result.score, 0.7881812)

if __name__ == "__main__":
    unittest.main()
