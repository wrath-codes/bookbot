import os


def get_book_text(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def get_word_count(text):
    return len(text.split())


def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in chars_dict:
            chars_dict[lowered_char] += 1
        else:
            chars_dict[lowered_char] = 1
    return chars_dict


def main():
    path_to_file = os.curdir + "/books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    word_count = get_word_count(book_text)
    chars_dict = get_chars_dict(book_text)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document.\n")
    for char in chars_dict:
        print(f"The '{char}' character was found {chars_dict[char]} times")

    print(f"--- End report ---")


main()
