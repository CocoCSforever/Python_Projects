# Yijia Ma: This is a username and password generating program which follows
# certain rules to generate a random result for user.
import random


# We output suggested username and password by
# first randomly pick integers and different parts of user input
# then concatenate each part
def main():
    # get user input for first name, last name, favorite word.
    f_name = input("Welcome to the username and password generator!\n\
Please enter your first name: ")
    l_name = input("Please enter your last name: ")
    f_word = input("Please enter your favorite word: ")

    # personalize a polite response and print out the user name
    # Add 7 * no matter we need it or not and then only pick the first
    # 8 chars and concatenate them with a random number between [0,99]
    user_name_temp = f_name.lower()[0] + l_name.lower() + "*"*7
    user_name = user_name_temp[0:8] + str(random.randint(0, 99))
    print(f"\nThank you {f_name}, your user name is {user_name}\n")

    # add each part of string together by rules and then replace certain pairs
    # of characters.
    passw1_temp = f_name.lower() + str(random.randint(0, 99)) + l_name.lower()
    passw1 = passw1_temp.replace("a", "@").replace("o", "0").replace("l", "1")\
        .replace("s", "$")

    # use lower and upper function to pick up certain letters from user input
    passw2 = f_name[0].lower() + f_name[len(f_name)-1].upper()\
        + l_name[0].lower() + l_name[len(l_name)-1].upper()\
        + f_word[0].lower() + f_word[len(f_word)-1].upper()

    # for each case, we should choose chars from 0 to a random index
    # which is less than string length. so the range of the random function
    # should be from 1 to length
    passw3 = f_name[0:random.randint(1, len(f_name))]\
        + l_name[0:random.randint(1, len(l_name))]\
        + f_word[0:random.randint(1, len(f_word))]

    # print the final results
    print("Here are three suggested passwords for you to consider:\n")
    print(f"""Password 1: {passw1}
Password 2: {passw2}
Password 3: {passw3}""")


main()
