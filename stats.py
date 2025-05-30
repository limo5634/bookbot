def count_words(text):
    wordList = text.split()
    num_words = 0
    num_words = len(wordList)
    return num_words
    #print(f"Found {num_words} total words.")

def count_chars(text):
    char_dict =  {}
    for char in text:
        key = char.lower()
        char_dict[key] = char_dict.get(key, 0) + 1
    return char_dict

def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
   
    # 1) Liste aus dict bauen, nur Buchstaben behalten
    entries = [
        {"char": ch, "num": cnt}
        for ch, cnt in char_counts.items()
        if ch.isalpha()
    ]
    # 2) absteigend nach "num" sortieren
    entries.sort(key=lambda e: e["num"], reverse=True)
    return entries