def main():
    a,b = input(), input()
    print(sum(1 for i, ch in enumerate(a) if ch != b[i]))

if __name__ == '__main__':
    main()
