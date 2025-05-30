import sys
from stats import count_words
from stats import count_chars
from stats import sort_char_counts

def get_book_text(path):
    bookText = ""
    with open(path) as text:
        bookText = text.read()
    return bookText



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    recievedString = get_book_text(path)
    print("----------- Word Count ----------")
    recievedCount = count_words(recievedString)
    print(f"Found {recievedCount} total words.")
        
    count_words(recievedString)
    recievedDict = count_chars(recievedString)
    sortedDict = sort_char_counts(recievedDict)
    print("--------- Character Count -------")
    for entry in sortedDict:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

main()