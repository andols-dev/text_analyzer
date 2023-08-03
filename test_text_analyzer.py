import unittest
from io import StringIO
from contextlib import redirect_stdout
from textanalyzer import TextAnalyzer
from unittest.mock import patch

class TestYourClass(unittest.TestCase):

    def test_is_there_input(self):
        analyzer = TextAnalyzer()
        test_text = "detta är ett test"

        self.assertIsNotNone(test_text)

if __name__ == '__main__':
    unittest.main()