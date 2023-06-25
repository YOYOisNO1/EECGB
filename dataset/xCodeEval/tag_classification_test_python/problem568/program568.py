def sum(a):
        s=0
        for i in a:
            s=s+i
        return s
def lst(a,k):
        x=[]
        for i in a:
            x.append(abs(k-i))
        return x
    n=int(input())
    a=list(map(int,input().split()))
    k=max(a)
    while 1:
        if sum(lst(a,k))>sum(a):
            break
        else:
            k+=1
    print(k)