def program822():
        n,a,b = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        for i in range(1,n+1):
            if i in a:
                print(1)
            elif i in b:
                print(2)