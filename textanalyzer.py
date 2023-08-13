class TextAnalyzer:
    # Reusable function to make the word alphanumeric
    def make_alphanumeric(self, word):
        cleaned_text = ''.join(ch for ch in word if ch.isalpha())
        return cleaned_text

    def how_many_words(self, text):
        # This method counts the occurrences of each word in the given text.
        sentence_map = {}
        print("Occurrences of each word in the text")

        for word in text.split():
            # Convert the word to lowercase to make the count case-insensitive and make sure it's alphanumeric
            sentence_map[self.make_alphanumeric(word).lower()] = 1 + sentence_map.get(word, 0)

        for word, count in sentence_map.items():
            # Print each word and its occurrence count
            print(f"{word}: {count}")

    def count_unique_words(self, text):
        # This method counts the number of unique words in the given text.
        unique_words = set()
        for word in text.split():
            # Convert the word to lowercase to make the count case-insensitive and make sure it's alphanumeric
            unique_words.add(self.make_alphanumeric(word).lower())
        return len(unique_words)

    def most_common_words(self, text, num_words):
        # This method returns the most common words and their occurrence count in the given text.
        word_freq = {}
        for word in text.split():
            # Convert the word to lowercase to make the count case-insensitive and make sure it's alphanumeric
            word_freq[self.make_alphanumeric(word).lower()] = word_freq.get(self.make_alphanumeric(word).lower(), 0) + 1

        # Sort the word frequencies in descending order based on occurrence count
        sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        return sorted_word_freq[:num_words]

    def menu(self):
        print("\nChoose an option:")
        menu = ["a. Most common words", "b. Count unique words", "c. Occurrences of each word", "x. Exit program" ]
        for menu_option in menu:
            print(f"{menu_option}")
            print("____________________________")

def main():
    # Initialize the TextAnalyzer class
    analyzer = TextAnalyzer()
    print("Welcome to Text Analyzer")
    # Loop until the user enters valid text to analyze
    while True:
        text = input("Add text that you want to analyze and press enter: \n")
        if text.strip():
            break
        print("Error: You must enter text to analyze")

    # Show menu
    analyzer.menu()

    # Choose a menu option
    while True:
        choice = input("Enter the letter of the option you want to run and press enter: \n")

        if choice == 'a':
            # Get the number of most common words from the user
            while True:
                try:
                    num_words = int(input("How many of the most common words do you want to see? Enter a number: "))
                    if num_words <= 0:
                        print("Please enter a positive number")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number")

            # Run the most_common_words method and display the result
            common_words = analyzer.most_common_words(text, num_words)
            print("Most common words in the text:")
            for word, count in common_words:
                print(f"{word}: {count}")
        elif choice == 'b':
            # Run the count_unique_words method and display the result
            unique_words_count = analyzer.count_unique_words(text)
            print(f"Number of unique words: {unique_words_count}")
        elif choice == 'c':
            # Run the how_many_words method and display the result
            analyzer.how_many_words(text)
        elif choice == 'x':
            # Exit the program
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
