def program151():
    n=input()
    m=map(int,input().split())
    c = 0
    while n > m[c]:
        n -= m[c]
        c = (c + 1)%7
    print(c) + 1    