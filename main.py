def main():
    book_path = "books/frankenstein.txt"
    text = get_book_content(book_path)
    words = get_number_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {words} of words!")
    chars = []
    chars = get_number_characters(text)
    print(chars)
    sorted_chars = sorted(chars.items(), reverse=True, key=lambda item: item[1])
    for key, value in sorted_chars:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_number_characters(text):
    lower_case_text = text.lower()
    splitted_text = list(lower_case_text)
    set_text = set(splitted_text)
    chars = {}
    for a in set_text:
        if a.isalpha():
            chars[a] = splitted_text.count(a)
    return chars

def get_number_words(text):
    words = text.split()
    return len(words)

def get_book_content(path):
    with open(path) as f:
        return f.read() 

main()