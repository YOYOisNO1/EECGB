def program4842():
    n,s = map(int, input().split())
    if s <= n:
        print(1)
    else:
        if s % n == 0:
            print(s//n)
        else:
            print(s//n+1)