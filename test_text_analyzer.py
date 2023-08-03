import unittest
from unittest.mock import patch
from textanalyzer import TextAnalyzer


class TestText(unittest.TestCase):

    def test_is_there_input(self):
        analyzer = TextAnalyzer()
        test_text = "detta är ett test"

        self.assertIsNotNone(test_text)

    def test_check_occurences(self):
        analyzer = TextAnalyzer()
        test_text = "Detta är ett test. Detta"

        expected_output = {
            "Detta": 2,
            "är":1,
            "ett": 1,
            "test":1,
        }

        with patch('builtins.print') as mock_print:
            analyzer.how_manywords(test_text)



        mock_print.assert_any_call("Occurrences of each word in the text")

    def test_check_occurences_lower(self):
        analyzer = TextAnalyzer()
        test_text = "Detta är ett test. detta"

        expected_output = {
            "Detta": 2,
            "är": 1,
            "ett": 1,
            "test": 1,
        }

        with patch('builtins.print') as mock_print:
            analyzer.how_manywords(test_text)

        mock_print.assert_any_call("Occurrences of each word in the text")

if __name__ == '__main__':
    unittest.main()