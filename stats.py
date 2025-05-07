def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def count_book_words(book_contents):
    nums_words = len(book_contents.split())
    return nums_words

def count_book_letters(book_contents):
    dictionary = {}
    for letter in book_contents:
        dictionary[letter.lower()] = dictionary.get(letter.lower(), 0) + 1
    return dictionary

def char_num_info(dictionary):
    char_nums = []
    for key in dictionary:
        if key.isalpha():
            char_nums.append({"char": key, "num": dictionary[key]})
    char_nums.sort(key=sort_on, reverse=True)
    return char_nums

# Sorting Method Key Function Helper
def sort_on(dict):
    return dict["num"]

def report(total_words, char_nums, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for letter_num in char_nums:
        print(f"{letter_num['char']}: {letter_num['num']}")
    print("============= END ===============")