def main():
    text = input()
    c, g = 0, 0
    skew = [0]
    for ch in text:
        if ch == 'C':
            c += 1
        if ch == 'G':
            g += 1
        skew.append(g-c)
    mn = min(skew)
    print(*[i for i, val in enumerate(skew) if val == mn])


if __name__ == '__main__':
    main()
