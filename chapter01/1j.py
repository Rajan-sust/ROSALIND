from collections import defaultdict
from itertools import product

def hamming_distance(a, b):
    return sum(1 for i, ch in enumerate(a) if ch != b[i])

def rev_complement(s):
    mp = {
        'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'
    }
    return ''.join([mp[ch] for ch in s])[::-1]

def main():
    text = input()
    k, d = map(int, input().split())
    n = len(text)
    mp = defaultdict(int)
    for k_mer in product('ACGT', repeat = k):
        s = ''.join(k_mer)
        for i in range(n-k+1):
            if hamming_distance(s, text[i:i+k]) <= d:
                mp[s] += 1
            if hamming_distance(rev_complement(s), text[i:i+k]) <= d:
                mp[s] += 1
    mx = max(mp.values())
    print(*[key for key, val in mp.items() if val == mx])




if __name__ == '__main__':
    main()
