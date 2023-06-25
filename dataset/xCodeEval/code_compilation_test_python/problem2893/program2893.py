def main():
    M = 100010
    a, m = map(int, input().split())
    s = [0] * M
    while s[a % m] == 0:
        s[a % m] = 1
        a += a % m
    if s[0]:
        print 'Yes'
    else:
        print 'No'
    main()