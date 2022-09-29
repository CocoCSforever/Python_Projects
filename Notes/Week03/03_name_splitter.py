fullname = input("Input your full name: ")

name_break = fullname.rfind(' ')

first_and_middle = fullname[:name_break]
last = fullname[name_break+1:]

print("Your name in last-name first format:")
print(f"{last}, {first_and_middle}")
