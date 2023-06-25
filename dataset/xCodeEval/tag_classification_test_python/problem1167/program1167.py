def program1167():
    k = int(input())
    s = "a"
    c = 0
    p = 1
    letters = "abcdefghijklmnopqstuvwxyz"
    l = 0
    while(c != k):
        c += p
        s += letters[l]
        p += 1
        if c+p > k:
            l += 1
            p = 0
    print(s)
        