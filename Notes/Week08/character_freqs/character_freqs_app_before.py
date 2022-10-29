"""A simple app for generating character frequencies from
a text. Unfortunately, the functionality is impossible to write
unit tests for, as it hasn't been broken into functions or
methods."""

import sys
import re


def main():
    file_name = sys.argv[1]
    char_counts = {}
    total_count = 0

    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return

    for line in f:
        # return a string of every match in the string
        chars = re.findall(r"\w", line.lower())
        for char in chars:
            total_count += 1
            if char in char_counts.keys():
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    print("\nCharacter counts dictionary:")
    print(char_counts)

    print("\nAnd as a sorted list:")
    sorted_counts = sorted(char_counts.items(),
                           key=lambda x: x[1],
                           reverse=True)

    print(sorted_counts)

    ROUND_PLACES = 2
    sorted_freqs = [(item, round((count/total_count), ROUND_PLACES))
                    for (item, count) in sorted_counts]

    print("\nSorted frequencies:")
    for ch in sorted_freqs:
        print(ch)


main()
