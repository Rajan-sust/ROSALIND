from collections import defaultdict
def main():
    text = input()
    k = int(input())
    mp = defaultdict(int)
    for i in range(len(text)-k+1):
        mp[text[i:i+k]] += 1
    mx = max(mp.values())
    print(*[key for key,val in mp.items() if val == mx])

if __name__ == '__main__':
    main()
