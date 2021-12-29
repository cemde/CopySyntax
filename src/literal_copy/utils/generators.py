import itertools
from string import ascii_lowercase, ascii_uppercase

def letters(length):
    if length == 0:
        return ""
    pool = itertools.cycle(ascii_uppercase + ascii_lowercase + "".join([str(x) for x in range(10)]))
    seq = []
    for letter in pool:
        seq.append(letter)
        if len(seq) >= length:
            break
    seq = "".join(seq)
    return seq
    