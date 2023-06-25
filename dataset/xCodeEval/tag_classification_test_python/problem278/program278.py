def main():
        l=lambda:map(int,input().split())
        n=input()
        a=l()
        x=a.index(1)
        x=max(x,n-1-x)
        y=a.index(n)
        y=max(y,n-1-y)
        print(max(x,y))
            
    main()