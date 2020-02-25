from collections import defaultdict

def main():
    text = input()
    k, L, t = map(int, input().split())
    mp = defaultdict(int)
    ans = list()
    for i in range(L-k+1):
        mp[text[i:i+k]] += 1
        if mp[text[i:i+k]] == t:
            ans.append(text[i:i+k])
    left = 0
    n = len(text)
    for i in range(L-k+1, n-k+1):
        mp[text[left:left+k]] -= 1
        left += 1
        mp[text[i:i+k]] += 1
        if mp[text[i:i+k]] == t:
            ans.append(text[i:i+k])
    print(*list(set(ans)))



if __name__ == '__main__':
    main()
