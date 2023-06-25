def program2115():
    n,d = map(int,input().split(' '))
    num = map(int,input().split(' '))
    m = input()
    num.sort()
    if m < n:
        print sum(num[0,m])
    else:
        print sum(num) - d*(m - n)