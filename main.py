from stats import word_counter
from stats import char_counter
from stats import dict_sorter
import sys

line_length = 33
analized_book = "books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as f:
            book_content = f.read()
            return book_content
    return ""

def line_printer(middle_string, line_char="-"):
    starting_index = round((line_length - len(middle_string)) / 2)
    printed_line = ""
    for index in range(0, line_length):
        if index == starting_index:
            printed_line = printed_line + middle_string
        elif index > starting_index and index < (starting_index + len(middle_string)):
            pass
        else:
            printed_line = printed_line + line_char
    print(printed_line)
            

def dict_printer(dicts):
    for dict in dicts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    line_printer(" BOOKBOT ", "=")
    analized_book = sys.argv[1]
    book_content = get_book_text(analized_book)
    print(f"Analyzing book found at {analized_book}")
    line_printer(" Word Count ", "-")
    words_number = word_counter(book_content)
    print(f"Found {words_number} total words")
    line_printer(" Character Count ", "-")
    counted_chars= char_counter(book_content)
    sorted_dicts = dict_sorter(counted_chars)
    dict_printer(sorted_dicts)
    line_printer(" END ", "=")


    
      

main()