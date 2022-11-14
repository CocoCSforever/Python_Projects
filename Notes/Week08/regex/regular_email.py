import re


my_string = "ABCDE12345abcdefgLMNOP"
# raw: take the string just as it is, treat it as a bare raw piece of string
# capture groups: match a particular part of string
# and match it in chunck with special name
# followed by 0 or more abstract characters, followed by one or more digits,
# followed by one or more lowercase characters, followed by 0 or more abstract characters
# greedy matching is default, changing it to lazy matching by r".*?([0-9]+)([a-z]+).*"
my_string = re.sub(r".*([0-9]+)([a-z]+).*", r"Matched \1 then \2", my_string)
# (\w+\.?)+@(\w+\.?)+
# .+@(\w+\.?)+    safi@gmail
# .+@(\w+\.+)+\w+
# .+@(\w+\.)+\w+
