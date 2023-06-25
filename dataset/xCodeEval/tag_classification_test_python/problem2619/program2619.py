def program2619():
    n = int(input())
    l = list(map(int,input().split()))
    f = 0
    for i in l:
        if(i):
            f = 1
            break
    if(f):
        print('hard')
    else:
        print('easy')