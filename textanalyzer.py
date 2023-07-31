class TextAnalyzer:
    def how_manywords(self,text):
        sentence_map = {}
        print("Occurrences of each word in the text")
        for word in text.split():
            sentence_map[word] = 1 + sentence_map.get(word, 0)

        for word,count in sentence_map.items():
            print(f"{word}: {count}")
def main():
    analyze = TextAnalyzer()

    print("Welcome to text analyzer")

    text = input("Add text that you want to analyze and press enter: ")
    analyze.how_manywords(text)




    #keyword_input = input("Add keyword that you want look for. Use space between every keyword: ")

    #keywords = keyword_input.split()


if __name__ == "__main__":
    main()