def program2611():
    n,a,b=[int(i) for i in input().split()]
    h=0
    for i in range(1,n+1):
        if i-1>=a and n-i<=b:
            h+=1
    print(h)