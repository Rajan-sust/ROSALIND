from itertools import product


def hamming_distance(a, b):
    return sum(1 for i, ch in enumerate(a) if ch != b[i])

def main():
    text, d = input(), int(input())
    ans = [''.join(kmer) for kmer in product('ACGT', repeat = len(text)) if hamming_distance(''.join(kmer), text) <= d]
    for s in ans:
        print(s)

if __name__ == '__main__':
    main()
