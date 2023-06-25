def program5220():
    n=int(input())
    l=list(map(int,list(input())))
    if(l.count(7)+l.count(4)==n and sum(l[:n//2])==sum(l)//2):
        print("YES")
    else:
        print("NO")