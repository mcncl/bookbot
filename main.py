#!/usr/bin/env python3

from stats import word_count, character_count, sort_counts
import sys


def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    character_list = character_count(get_book_text(sys.argv[1]))
    sorted_list = sort_counts(character_list)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
{word_count(get_book_text(sys.argv[1]))}
--------- Character Count -------
""")

    for entry in sorted_list:
        print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")

main()
