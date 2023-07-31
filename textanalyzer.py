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
    analyze = TextAnalyzer()

    print("Welcome to text analyzer")

    while True:
        text = input("Add text that you want to analyze and press enter: ")
        if text.strip():
            break
        print("Error: You must enter text to analyze")

    while True:
        try:
            num_words = int(input("Enter the number of most common words to display: "))
            if num_words <= 0:
                print("Please enter a positive number")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number")

    common_words = analyze.most_common_words(text, num_words)
    print("Most common words in the text:")
    for word, count in common_words:
        print(f"{word}: {count}")

    all_analyzed = False
    while True:
        choice = input("Do you want to run analysis methods (yes/no): ")
        if choice.lower() == 'yes':
            if not all_analyzed:
                print(f"Unique words: {analyze.count_unique_words(text)}")
                analyze.how_manywords(text)
                all_analyzed = True
            else:
                print("All analysis methods have already been run.")
                break
        elif choice.lower() == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



if __name__ == "__main__":
    main()
