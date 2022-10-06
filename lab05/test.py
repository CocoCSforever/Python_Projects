import re


def main():
    filename = input("Enter the file name: ")
    try:
        file = open(filename, "r", encoding="utf-8")
    except OSError as e:
        print("Can't open", filename)
        return

    char_count = 0
    alphanumeric_count = 0

    # read the whole file and split by whitespace and new lines
    file_string = file.read()
    word_count = len(file_string.split())
    file_str = file_string.replace(" ", "")
    char_count = len(file_str)
    alphanumeric_count = len(re.findall(r"\w", file_str))
    # for word in word_list:
    #    char_count += len(word)
    #    alphanumeric_count += len(re.findall(r"\w", word))

    # Another version: first set three variables to 0
    # for line in file:
        # split by whitespace to get a list of words
        # word_list = line.strip().split()
        # for word in word_list:
        #    alphanumeric_count += len(re.findall(r"\w", word))
        #    char_count += len(word)
        # word_count += len(word_list)

    print(f"Words: {word_count}\nCharacters: {char_count} \
\nLetters & numbers: {alphanumeric_count}")


main()
