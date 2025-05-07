import sys

from stats import (
    get_book_text,
    count_book_words,
    count_book_letters,
    char_num_info,
    report
    )

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]

    book_contents = get_book_text(book)
    total_words = count_book_words(book_contents)
    total_letters = count_book_letters(book_contents)
    char_nums = char_num_info(total_letters)
    
    report(total_words, char_nums, book)

if __name__ == "__main__":
    main()