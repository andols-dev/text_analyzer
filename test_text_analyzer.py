import unittest
from unittest.mock import patch
from textanalyzer import TextAnalyzer

class TestText(unittest.TestCase):
    def test_is_there_input(self):
        # Create an instance of the TextAnalyzer class
        analyzer = TextAnalyzer()

        # Define the test_text to analyze
        test_text = "detta är ett test"

        # Check if the test_text is not None
        self.assertIsNotNone(test_text)

    def test_check_occurences(self):
        # Create an instance of the TextAnalyzer class
        analyzer = TextAnalyzer()

        # Define the test_text to analyze
        test_text = "Detta är ett test. Detta"

        # Define the expected_output with the occurrence count of each word in the test_text
        expected_output = {
            "Detta": 2,
            "är": 1,
            "ett": 1,
            "test": 1,
        }

        # Use patch to mock the 'print' function to avoid printing during the test
        with patch('builtins.print') as mock_print:
            # Call the how_manywords method with the test_text
            analyzer.how_many_words(test_text)

        # Assert that the "Occurrences of each word in the text" is printed during the method call
        mock_print.assert_any_call("Occurrences of each word in the text")

    def test_check_occurences_lower(self):
        # Create an instance of the TextAnalyzer class
        analyzer = TextAnalyzer()

        # Define the test_text to analyze
        test_text = "Detta är ett test. detta"

        # Define the expected_output with the occurrence count of each word in the test_text
        expected_output = {
            "Detta": 2,
            "är": 1,
            "ett": 1,
            "test": 1,
        }

        # Use patch to mock the 'print' function to avoid printing during the test
        with patch('builtins.print') as mock_print:
            # Call the how_manywords method with the test_text
            analyzer.how_many_words(test_text)

        # Assert that the "Occurrences of each word in the text" is printed during the method call
        mock_print.assert_any_call("Occurrences of each word in the text")

    def test_most_common_words(self):
        # Create an instance of the TextAnalyzer class
        analyzer = TextAnalyzer()

        # Define the test_text to analyze
        test_text = "Detta är ett test Bara ett test Ett fungerande test"

        # Define the number of most common words to retrieve
        num_words = 2

        # Define the expected_output with the two most common words and their occurrence count in the test_text
        expected_output = [
            ("ett", 3),
            ("test", 3)
        ]

        # Call the most_common_words method with the test_text and num_words
        common_words = analyzer.most_common_words(test_text, num_words)

        # Assert that the common_words list is equal to the expected_output list
        self.assertEqual(common_words, expected_output)

if __name__ == '__main__':
    unittest.main()
