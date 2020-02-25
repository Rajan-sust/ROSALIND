def main():
    num, k = int(input()), int(input())
    mp = {
        0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'
    }
    pattern = ''
    for _ in range(k):
        pattern += mp[num%4]
        num //= 4
    print(pattern[::-1])

if __name__ == '__main__':
    main()
