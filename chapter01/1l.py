def main():
    text = input()
    mp = {
        'A' : 0, 'C': 1, 'G' : 2, 'T': 3        
    }
    num = 0
    for ch in text:
        num = num * 4 + mp[ch]
    print(num)

if __name__ == '__main__':
    main()
