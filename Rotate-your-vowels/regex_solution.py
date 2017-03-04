import re

string = 'The quick brown fox jumps over the lazy dog'
sub_function = lambda x: 'eiouaEIOUA'['aeiouAEIOU'.find(x.group(0))]

for x in range(20):
    string = re.sub('(?i)[aeiou]', sub_function, string)
    print(string)
