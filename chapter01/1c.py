def main():
    text = input()
    mp = {
            'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'
    }
    print(''.join([mp[ch] for ch in text])[::-1])
if __name__ == '__main__':
    main()
