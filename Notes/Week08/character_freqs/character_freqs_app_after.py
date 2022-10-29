# More testable implementation

import sys
from character_freqs import CharFreqs


def main(file_name):
    cf = CharFreqs()

    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return

    for line in f:
        # Feed each line to cf
        cf.count_line(line)

    print("\nChracter counts dictionary:")
    print(cf.char_counts)

    print("\nAnd as a sorted list:")
    print(cf.sorted_counts)

    print("\nCharacter freqs dictionary:")
    print(cf.char_freqs)

    print("\nSorted frequencies:")
    for ch in cf.sorted_freqs:
        print(ch)


main(sys.argv[1])
