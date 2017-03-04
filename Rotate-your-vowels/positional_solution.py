string = 'The quick brown fox jumps over the lazy dog'

for x in range(20):
    string = ''.join(['eiouaEIOUA' + c][0]['aeiouAEIOU'.find(c)] for c in string)
    print(string)
