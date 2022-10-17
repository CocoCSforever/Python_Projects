import random

num = random.randint(1, 50)
user_guess=int(input("Welcome to the Guessing Game!\nI picked a number between 1 and 50. Try and guess!\n"))
tries=1

while (num != user_guess):
    if(user_guess>=num-1 and user_guess<=num+1):
        res="scalding hot"
    elif(user_guess>=num-2 and user_guess<=num+2):
        res="extremely warm"
    elif(user_guess>=num-3 and user_guess<=num+3):
        res="very warm"
    elif(user_guess>=num-5 and user_guess<=num+5):
        res="warm"
    elif(user_guess>=num-8 and user_guess<=num+8):
        res="cold"
    elif(user_guess>=num-13 and user_guess<=num+13):
        res="very cold"
    elif(user_guess>=num-20 and user_guess<=num+20):
        res="extremely cold"
    else:
        res="icy freezing miserably cold"
    tries+=1
    user_guess=int(input(f"You guessed {user_guess}\nYour guess is" +res\n))

if(tries==1):
    com="That was lucky!"
elif(tries>=2 and tries<=4):
    com="That was amazing!"
elif(tries==5 or tries==6):
    com="That was okay."
elif(tries==7):
    com="Meh."
elif(tries==8 or tries==9):
    com="This is not your game."
else:
    com="You are the worst guesser I've ever seen."


print(f"Congratulations. You figured it out in {tries} tries. {com}")