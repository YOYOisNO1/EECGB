def program1424():
    n = int(input())
    a = list(map(int,input().split()))
    if a.count(min(a)) > n//2:
        print('Bob')
    else:
        print('Alice')