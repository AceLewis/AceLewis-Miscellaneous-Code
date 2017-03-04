string = 'The quick brown fox jumps over the lazy dog'

for _ in range(20):
    string = string.translate(str.maketrans('aeiouAEIOU', 'eiouaEIOUA'))
    print(string)
