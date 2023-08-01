class TextAnalyzer:
    def how_manywords(self,text):
        sentence_map = {}
        print("Occurrences of each word in the text")
        for word in text.split():
            sentence_map[word.lower()] = 1 + sentence_map.get(word, 0)

        for word,count in sentence_map.items():
            print(f"{word}: {count}")

    def count_unique_words(self,text):
        unique_words = set()
        for word in text.split():
            unique_words.add(word.lower())
        return len(unique_words)

    def most_common_words(self,text,num_words):
        word_freq = {}
        for word in text.split():
            word_lower = word.lower()
            word_freq[word_lower] = word_freq.get(word_lower,0) + 1

        sorted_word_freq = sorted(word_freq.items(),key=lambda item: item[1], reverse=True)
        return sorted_word_freq[:num_words]

def main():
    analyzer = TextAnalyzer()

    print("Welcome to textanalyzer")

    while True:
        text = input("Add text that you want to analyze and press enter: \n")
        if text.strip():
            break
        print("Error: You must enter text to analyze")

    while True:
        print("\nChoose an option:")
        print("a. Most common words")
        print("b. Count unique words")
        print("c. Occurrences of each word")
        print("x. Exit program")

        choice = input("Enter the letter of the option you want to run and press enter: \n")

        if choice == 'a':
            while True:
                try:
                    num_words = int(input("How many of the most common words do you want to see? Enter a number: "))
                    if num_words <= 0:
                        print("Please enter a positive number")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number")

            common_words = analyzer.most_common_words(text, num_words)
            print("Most common words in the text:")
            for word, count in common_words:
                print(f"{word}: {count}")
if __name__ == "__main__":
    main()
