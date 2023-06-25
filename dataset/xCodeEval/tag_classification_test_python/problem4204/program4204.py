def program4204():
    n,k = map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    c=0
    while (s/n<k-0.5):
        s+=k
        n+=1
        c+=1
    print(c)