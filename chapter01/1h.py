def hamming_distance(a,b):
    return sum(1 for i,ch in enumerate(a) if ch != b[i])

def main():
    pattern, text, d = input(), input(), int(input())
    n, k = len(text), len(pattern)
    print(*[i for i in range(n-k+1) if hamming_distance(pattern, text[i:i+k]) <= d])

if __name__ == '__main__':
    main()
