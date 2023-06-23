def program1587():
    n,m = map(int, input().split())
    moves=0
    while n != m:
        moves+=1
        m += 1 if m % 2 != 0 or m < n else m=m//2
    print(moves)