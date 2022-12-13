def update_scores(a):
    score = a
    try:
        out = open("scores.txt", "r+")
        # "w" or "w+" will erase the file with the same name
        # but "w" cannot read
        # "r+" for both reading and writing
        # Difference between "r+" and "a+"
        # 1. if file doesn't exist, r and r+ throw an error
        # while a and a+ creates a new file
        # 2. r for only reading, a for only writing
        # 3. r+ and a+ both for reading and writing
        # 4. r/w file pointer at the beginning of the file
        # while a file pointer at the end of the file
    except OSError as e:
        print("Can't open scores.txt for writing.")
        return

    content = out.read()
    print(content)
    line_break = content.find('\n')
    line = content[:line_break]
    # if don't use strip, would include \n at the end of para
    # line = out.readline().strip()
    print(line)
    new_line = "test_player" + " " + str(score) + "\n"
    if line:
        score_break = line.rfind(' ')
        highest_score = int(line[score_break+1:])
        print("highest_score:", highest_score)
        if score > highest_score:
            content = new_line + content
        else:
            content = content + new_line
    print(content)
    out.seek(0)
    out.write(content)

    #     if score > highest_score:
    #         out.seek(0)
    #     else:
    #         out.seek(0, 2)
    # out.write("Test_player " + str(score) + "\n")


update_scores(19)
