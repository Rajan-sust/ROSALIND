from collections import defaultdict
from itertools import product

def main():
    text, k = input(), int(input())
    n = len(text)
    mp = defaultdict(int)
    for i in range(n-k+1):
        mp[text[i:i+k]] += 1
    print(*[mp[''.join(kmer)] for kmer in product('ACGT', repeat = k)])

if __name__ == '__main__':
    main()
