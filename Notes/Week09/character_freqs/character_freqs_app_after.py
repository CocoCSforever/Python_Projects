# More testable implementation
# The character frequency calculation logic has been
# removed from "main" and placed into its own class.
# This makes it possible to write tests for that functionality.
import sys

from character_freqs import CharFreqs


def main(file_name):
    # We create an instance of CharFreqs. This object (cf)
    # will do the character-counts-related work.
    cf = CharFreqs()

    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return

    for line in f:
        # We feed each line to cf.
        cf.count_line(line)

    print("\nCharacter counts dictionary:")
    # We print out the char_counts attribute from cf.
    # Note in the class that this is an actual attribute, not a method
    print(cf.char_counts)

    print("\nAnd as a sorted list:")
    # We print out sorted_counts. This also looks like an attribute
    # from our perspective here (note that it is not called with
    # parentheses). However, behind the scenes in the class it's
    # actually a method, not an attribute! The use of @property
    # in the class lets us obscure that fact to have a more
    # consistent interface here.
    print(cf.sorted_counts)

    print("\nCharacter freqs dictionary:")
    # char_freqs is also a method with a @property decorator
    print(cf.char_freqs)

    print("\nSorted frequencies:")
    # likewise sorted_freqs
    for ch in cf.sorted_freqs:
        print(ch)


main(sys.argv[1])
