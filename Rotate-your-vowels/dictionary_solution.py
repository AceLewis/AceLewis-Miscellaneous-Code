string = 'The quick brown fox jumps over the lazy dog'

letter_dict = dict(zip('aeiouAEIOU', 'eiouaEIOUA'))

for _ in range(20):
    string = ''.join(letter_dict.get(x, x) for x in string)
    print(string)
