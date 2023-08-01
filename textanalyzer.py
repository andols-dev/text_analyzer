class TextAnalyzer:
    def how_manywords(self, text):
        # This method counts the occurrences of each word in the given text.
        sentence_map = {}
        print("Occurrences of each word in the text")
        for word in text.split():
            # Convert the word to lowercase to make the count case-insensitive
            sentence_map[word.lower()] = 1 + sentence_map.get(word, 0)

        for word, count in sentence_map.items():
            # Print each word and its occurrence count
            print(f"{word}: {count}")

    def count_unique_words(self, text):
        # This method counts the number of unique words in the given text.
        unique_words = set()
        for word in text.split():
            # Convert the word to lowercase to make the count case-insensitive
            unique_words.add(word.lower())
        return len(unique_words)

    def most_common_words(self, text, num_words):
        # This method returns the most common words and their occurrence count in the given text.
        word_freq = {}
        for word in text.split():
            # Convert the word to lowercase to make the count case-insensitive
            word_lower = word.lower()
            word_freq[word_lower] = word_freq.get(word_lower, 0) + 1

        # Sort the word frequencies in descending order based on occurrence count
        sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        return sorted_word_freq[:num_words]


def main():
    # Initialize the TextAnalyzer class
    analyzer = TextAnalyzer()

    print("Welcome to textanalyzer")

    # Loop until the user enters valid text to analyze
    while True:
        text = input("Add text that you want to analyze and press enter: \n")
        if text.strip():
            break
        print("Error: You must enter text to analyze")

    # Main loop to display the menu and execute the chosen analysis method
    while True:
        print("\nChoose an option:")
        print("a. Most common words")
        print("b. Count unique words")
        print("c. Occurrences of each word")
        print("x. Exit program")

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
            # Run the how_manywords method and display the result
            analyzer.how_manywords(text)
        elif choice == 'x':
            # Exit the program
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
