print("We present the following facts for your",
      "personal edification:")

print("We present the following facts for your "+
      "personal edification:")

# numerical characters can be part of a string
print("Letters in the Hawaiian alphabet: 12")

# # concatenating strings with numbers results in a string
print("Total number of Japanese hiragana:", 46)

# # concatenating numbers and strings with plus require
# # explicitly "casting" the number to a string using str()
print("Total number of Japanese katakana: " + str(46))

# arithmetic and other expressions can be evaluated
# and converted to a string
print("672", "+", "5", "=", 672 + 5)

print(1, "is the loneliest number")

print("The speed limit on the highway in France is", 130, "km/h")

speed = 130
other_speed = 110
print(f"The speed limit on the highway in Italy is {speed} km/h. Another speed is {100 + 10}")

print("Here is a line\nHere is another line\nHere's a backslash: \\")

print("""Area and population of cities
\tTokyo\t847 sq miles\t13.96 million
\tLA\t502 sq miles\t3.973 million
\tLondon\t607 sq miles\t8.982 million
\tMumbai\t233 sq miles\t12.44 million
""")