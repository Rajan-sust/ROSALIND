def main():
    text, pattern = input(), input()
    n, k = len(text), len(pattern)
    count = 0
    for i in range(n-k+1):
        if text[i:i+k] == pattern:
            count += 1
    print(count)
if __name__ == '__main__':
    main()
