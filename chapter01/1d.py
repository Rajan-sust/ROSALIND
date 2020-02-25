def main():
    pattern, text = input(), input()
    n,k = len(text), len(pattern)
    print(*[i for i in range(n-k+1) if text[i:i+k] == pattern])
if __name__ == '__main__':
    main()
