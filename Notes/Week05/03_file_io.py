import sys


def main(files):
    """
    Summerizes poems
    """
    # 'w' for creating a new file for writing
    try:
        # w for overwrite, a for append, r for read
        out = open("results.txt", "w")
        # if fails, throw an exception
        # OSError is a general kind of error:
        # means something has gone wrong at the operating system
        # create an OSError object as e, has some information
    except OSError as e:
        print("Can't open results.txt for writing")
        return

    for filename in files:
        try:
            f = open(filename, "r", encoding="utf-8")
        except FileNotFoundError as e:
            print("Can't open", filename)
            return

        # strip: get rid of any subsequent whitespace or new lines before and
        # after the string
        title = f.readline().strip()
        # eliminate "By", the first word in the author line
        author = ' '.join(f.readline().strip().split()[1:])
        print("Title: ", title)
        print("Author: ", author)

        line_count = 0
        for _line in f:
            line_count += 1

        out.write("Processed poem:\n")
        out.write(f"Title: {title}\n")
        out.write(f"Author: {author}\n")
        out.write(f"Lines: {line_count}\n")
        out.write("\n")

    # write in the file, if the file already exists, it will overwrite it
    # out.write("Hello output again!")
    # print(files)


main(sys.argv[1:])
