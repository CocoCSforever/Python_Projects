def main():
    answer = input("Please answer yes or no: ")
    #while(not (answer == "yes" or answer =="no")):
    while(answer != "yes" and answer !="no"):
        # replace False with an appropriate condition
        answer = input("You must answer 'yes' or 'no': ")
    print("Thank you for your satisfactory answer.")


if __name__ == '__main__':
    main()
