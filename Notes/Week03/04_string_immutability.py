phrase = "Change is inevitable"

print("Original string: ", phrase)
print("Length of string: ", len(phrase))

mutation1 = phrase + " except from vending machines"
print(f"1: {mutation1}")

mutation2 = mutation1.upper()
print(f"2: {mutation2}")

mutation3 = mutation2.replace(" ", "X")
print(f"3: {mutation3}")

print(f"Mutation 3 is {len(mutation3)} characters long.")

mutation4 = mutation3 + "\n"

print(f"4: {mutation4}")

print("That was mutation4")
print(f"Mutation 4 is {len(mutation4)} characters long.")

print(f"Original phrase: {phrase}")

# phrase[0] = 'Z'

print(phrase[0])

phrase = "Zhange is inevitable"

print(phrase)
