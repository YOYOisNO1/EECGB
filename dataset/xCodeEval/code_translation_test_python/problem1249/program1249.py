def program1249():
    k,a,b=map(int,input().split())
    u=int(a/k)+int(b/k)
    if (a<k) and (b%k) :
        u=-1
    if (b<k) and (a%k):
        u=-1
    print(u)