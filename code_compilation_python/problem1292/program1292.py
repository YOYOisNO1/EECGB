def program1292():
    n,a,x,b,y=list(map(int,input().split()))
    while True:
        if a==b:
            print("YES")
            return 0
        if (a==x or b==y):
            
            break
        a=(a+1)%n
        b=(b-1+n)%n
    print("NO")