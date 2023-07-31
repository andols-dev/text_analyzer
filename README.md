# Text Analyzer

## Overview
Text Analyzer is a Python console application that allows users to analyze text by performing various operations. The program provides three main analysis methods:

1. **Word Occurrences:** This method counts the occurrences of each word in the input text and displays the results.

2. **Count Unique Words:** This method calculates the number of unique words in the input text and prints the count.

3. **Most Common Words:** Users can specify the number of most common words they want to display, and the program will output those words along with their occurrence counts in descending order.

## How to Use
1. **Welcome Message:** When you run the program, you will be greeted with a welcome message and asked to input the text you want to analyze.

2. **Input Text:** Enter the text you want to analyze, and the program will validate that you have provided some input. If you haven't entered any text, it will prompt you to do so.

3. **Common Words:** Next, you'll be asked to input the number of most common words you want to display. Enter a positive integer to proceed.

4. **Options Menu:** The program will then ask if you want to run other analysis methods. If you choose "yes," it will display the count of unique words and the occurrences of each word in the text.

5. **Exiting the Program:** You can choose "no" when asked if you want to run other analysis methods, which will exit the program and display the exit message.

## Dependencies
The Text Analyzer program has no external dependencies and is written entirely in Python.

## How to Run
To run the program, simply execute the `main()` function in the `text_analyzer.py` file. You can run the script from the command line or use an integrated development environment (IDE) to execute the program.

## Note
The program ensures that valid input is provided for the number of common words, and it will continue to ask for input until a valid positive integer is entered.
