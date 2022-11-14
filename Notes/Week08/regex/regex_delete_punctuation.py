import re

a_string = "!hi. wh?at is the weat[h]er lik?e."
new_string = re.sub(r'[^\w\s]', '', a_string)
print(new_string)
