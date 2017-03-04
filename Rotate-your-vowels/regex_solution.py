import re

string = 'The quick brown fox jumps over the lazy dog'

for x in range(20):
    string = re.sub('(?i)[aeiou]', lambda x: 'eiouaEIOUA'['aeiouAEIOU'.find(x.group(0))], string)
    print(string)
