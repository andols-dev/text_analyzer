import pyperclip
class TextAnalyzer:
    def text_analyzer(self,text,keywords):
        raise NotImplementedError("Denna del av koden är inte implementerad ännu.")

def main():
    analyze = TextAnalyzer()

    print("Welcome to text analyzer")
    print("Copy text from, for example, a webpage or document.")


    # The text that user copies will be added to clipboard and will be inserted in sentence
    sentence = pyperclip.paste()

    # Check if user has copied text
    if sentence:
        print("This is the text that you want analyze")
        print(sentence)

    keyword_input = input("Add keyword that you want look for. Use space between every keyword")
    raise NotImplementedError("Denna del av koden är inte implementerad ännu.")


if __name__ == "__main__":
    main()