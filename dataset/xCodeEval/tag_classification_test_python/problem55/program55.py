def digitsum(n):
        n=list(map(int,str(n)))
        if sum(n)%4==0:
            return True
        else:
            return False
    n=int(input())
    for i in range(n,n+10):
        if digitsum(i):
            print(i)
            break