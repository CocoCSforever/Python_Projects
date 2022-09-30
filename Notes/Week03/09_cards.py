suit = input("Input a card suit: ").lower()
value = input("Input a card value: ").lower()

if (suit == "diamond" or suit == "heart"):
    color = "red"
else:
    color = "black"

if (value == "king" or value == "queen" or value == "jack"):
    is_face_card = True
else:
    is_face_card = False

if (color == "red"):
    if is_face_card:
        print("You chose a red face card")
    else:
        print("You chose a red pip card")
else:
    if is_face_card:
        print("You chose a black face card")
    else:
        print("You chose a black pip card")
