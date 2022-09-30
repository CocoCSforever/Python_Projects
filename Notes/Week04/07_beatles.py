band = ["Paul", "Pete", "John", "George"]
instruments = ["Bass", "Drums", "Vocals", "Guitar"]


print(band)
print(len(band))

print(instruments[1])
print(instruments[1:])
# the element and the rest of the list
print(instruments[1:3])
# the element before the index 3

band[1] = "Ringo"

print(band)

for member in band:
    print("Introducing", member)

lineup = zip(band, instruments)
# zip takes two sequence. actually iterative, once done, it would be empty
# and create a sequence of pairs that original sequence zipps in order
# item by item. lineup_list=list(lineup) would fix the problem 
# that lineip can only be used once

# for member in lineup:
#    print(member)


print(lineup)
# zip object at memory location
print(list(lineup))


# print(lineup_list)
# print(lineup_list[1][2])
print(instruments[-1])
lineup1 = list(zip(range(10), band, instruments))
print(lineup1)

for m in lineup1:
    print(m[0], m[1], m[2])
