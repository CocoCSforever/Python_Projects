import re


def main():
    # get user input of filename
    filename = input("Enter the file name: ")
    # read file and get a file object
    try:
        file = open(filename, "r", encoding="utf-8")
    except OSError as e:
        print("Can't open", filename)
        return

    word_count = 0
    char_count = 0
    alphanumeric_count = 0

    # get rid of any whitespace or new lines before and after
    for line in file:
        # split by whitespace to get a list of words
        word_list = line.strip().split()
        word_count += len(word_list)

        # remove whitespce for each line
        line_string = line.strip().replace(" ", "")
        char_count += len(line_string)
        # re return a list of all matched "\w" char in line_string
        alphanumeric_count += len(re.findall(r"\w", line_string))

    print(f"Words: {word_count}\nCharacters: {char_count} \
\nLetters & numbers: {alphanumeric_count}")


main()
