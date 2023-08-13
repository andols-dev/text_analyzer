class TextAnalyzer:
    @staticmethod
    def make_alphanumeric(word):
        """
        Make the word alphanumeric.
        :param word: The input word.
        :return: The cleaned alphanumeric text.
        """
        cleaned_text = ''.join(ch for ch in word if ch.isalpha())
        return cleaned_text

    @staticmethod
    def how_many_words(text):
        """
        Count the occurrences of each word in the given text.
        :param text: The input text.
        """
        word_occurences = {}
        print("Occurrences of each word in the text")

        for word in text.split():
            word_occurences[TextAnalyzer.make_alphanumeric(word).lower()] = 1 + word_occurences.get(word, 0)

        for word, count in word_occurences.items():
            print(f"{word}: {count}")

    def count_unique_words(self, text):
        """
        Count the number of unique words in the given text.
        :param text: The input text.
        :return: The number of unique words.
        """
        unique_words = set()
        for word in text.split():
            unique_words.add(TextAnalyzer.make_alphanumeric(word).lower())
        return len(unique_words)

    @staticmethod
    def most_common_words(text, num_words):
        """
        Return the most common words and their occurrence count in the given text.
        :param text: The input text.
        :param num_words: The number of most common words to retrieve.
        :return: A list of tuples containing the most common words and their counts.
        """
        word_freq = {}
        for word in text.split():
            word_freq[TextAnalyzer.make_alphanumeric(word).lower()] = word_freq.get(TextAnalyzer.make_alphanumeric(word).lower(), 0) + 1

        sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        return sorted_word_freq[:num_words]

    @staticmethod
    def menu():
        """
        Display the menu options.
        """
        print("\nChoose an option:")
        menu = ["a. Most common words", "b. Count unique words", "c. Occurrences of each word", "x. Exit program"]
        for menu_option in menu:
            print(f"{menu_option}")
            print("____________________________")

    @staticmethod
    def choose_how_many_words():
        """
        Prompt the user for the number of most common words to show.
        :return: The number of most common words.
        """
        while True:
            try:
                num_words = int(input("How many of the most common words do you want to see? Enter a number: "))
                if num_words <= 0:
                    print("Please enter a positive number")
                else:
                    return num_words
            except ValueError:
                print("Invalid input. Please enter a number")

    def choose_menu_option(self, text):
        """
        Prompt the user to choose a menu option and perform the chosen action.
        :param text: The input text.
        """
        while True:
            choice = input("Enter the letter of the option you want to run and press enter: \n")

            if choice == 'a':
                num_words = TextAnalyzer.choose_how_many_words()
                common_words = TextAnalyzer.most_common_words(text, num_words)
                print("Most common words in the text:")
                for word, count in common_words:
                    print(f"{word}: {count}")
            elif choice == 'b':
                unique_words_count = self.count_unique_words(text)
                print(f"Number of unique words: {unique_words_count}")
            elif choice == 'c':
                TextAnalyzer.how_many_words(text)
            elif choice == 'x':
                print("Exiting...")
                break


def main():
    analyzer = TextAnalyzer()
    print("Welcome to Text Analyzer")
    while True:
        text = input("Add text that you want to analyze and press enter: \n")
        if text.strip():
            break
        print("Error: You must enter text to analyze")

    TextAnalyzer.menu()
    analyzer.choose_menu_option(text)


if __name__ == "__main__":
    main()
