import unittest
from io import StringIO
from contextlib import redirect_stdout
from textanalyzer import TextAnalyzer
class TestYourClass(unittest.TestCase):

    def test_how_manywords(self):
        # Test with a simple text
        text = "this is a simple test text to count the word occurrences"
        expected_output = "Occurrences of each word in the text\nthis: 1\nis: 1\na: 1\nsimple: 1\ntest: 1\ntext: 1\nto: 1\ncount: 1\nthe: 1\nword: 1\noccurrences: 1\n"

        # Redirect stdout to a StringIO buffer
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            # Call the method that prints the output
            text_analyzer = TextAnalyzer()
            text_analyzer.how_manywords(text)

        # Get the captured output
        output = captured_output.getvalue()
        # Compare the captured output with the expected output
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()