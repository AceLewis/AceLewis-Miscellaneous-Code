import re

def hipsterpy(string):
    return re.sub(r"(?i)([^\s])[aeiou]([^aeiou]*)\b", r'\1\2', string)

strings = "A Hipster follows the latest trends and fashions."

print(hipsterpy(strings))
