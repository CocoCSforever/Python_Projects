my_string = "Hello for loops"


for my_character in my_string:
    print("Character:", my_character)


print("The value of my_character now is:", my_character)

HOW_HIGH_TO_COUNT = 10

# range can take two argus, the 1st one is the starting point of edge
# (inclusive), the 2nd is not inclusive
# thus one number larger than edge

# 1-9
for i in range(1, HOW_HIGH_TO_COUNT):
    print("Value:", i)


# from 0-9
for i in range(HOW_HIGH_TO_COUNT):
    print("Value:", i)

# 3rd == how much we are skipping by
for i in range(1, HOW_HIGH_TO_COUNT, 2):
    print("Value:", i)

# range(0,10)
print(range(10))
# if we want to print out the whole sequence, we should convert it into list
#[0,1,2,3,4,5,6,7,8,9] enclosed by square brackets and it's a sequence of numbers
print(list(range(10)))
