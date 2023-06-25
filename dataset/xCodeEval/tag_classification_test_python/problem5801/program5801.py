def program5801():
    n = int(input())
    a = list(map(int,input().split()))
    min1 = min(a)
    if(a.count(min1) > n//2 ):
        print('Bob')
    else:
        print('Alice')