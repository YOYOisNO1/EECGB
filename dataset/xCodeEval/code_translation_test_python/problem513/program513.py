def program513():
    n=int(input())
    for i in range(n):
        b=list(map(int,input().split()))
        c=list(map(int,input().split()))
        d=b+c 
        if d.count(1)==0:
            print(0)
        elif d.count(1)==4:
            print(2)
        else:
            print(1)