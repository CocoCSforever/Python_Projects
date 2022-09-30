
def main():
    command = None
    while (command != 'stop'):
        command = in_lower("What do you want me to do? ")
        print(f"Okay, I'll {command}")
    print("Whew! Good to be done!")


def in_lower(prompt):
    return input(prompt).lower()


main()
