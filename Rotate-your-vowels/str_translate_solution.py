def rotate(li, x):
    return li[-x % len(li):] + li[:-x % len(li)]


def str_rotate(_str, letters, rot_num):
    match_ltr = letters + letters.upper()
    replace_ltr = rotate(letters, rot_num)
    replace_ltr = replace_ltr + replace_ltr.upper()
    return _str.translate(str.maketrans(match_ltr, replace_ltr))


_str = 'The quick brown fox jumps over the lazy dog'
letters = 'aeiou'
rotate_by = -1

for _ in range(20):
    _str = str_rotate(_str, letters, rotate_by)
    print(_str)
