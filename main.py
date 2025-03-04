import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = read_book(path)
    
    num_words = count_words(content)
    
    num_chars = count_chars(content)
    sorted_num_chars = sort_num_chars(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_num_chars:
        if not char["name"].isalpha():
            continue
        print(f"{char["name"]}: {char["count"]}")


if __name__ == "__main__":
    main()

