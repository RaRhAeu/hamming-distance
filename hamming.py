import sys
import binascii
from collections import Counter


def hamming_dist(s1, s2):
    b1 = binascii.unhexlify(s1)
    b2 = binascii.unhexlify(s2)
    assert len(b1) == len(b2)
    res = len(b1)*8
    for x,y in zip(b1,b2):
        d = Counter(bin(x^y))['1']
        res -= d
    return res

if __name__ == '__main__':
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    zeros = hamming_dist(s1,s2)
    hdist = 1 - (zeros/(len(s1)*4))
    print(f"Equal bits: {zeros}")
    print(f"Hamming distance: {hdist}")
