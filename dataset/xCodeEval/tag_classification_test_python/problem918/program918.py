def program918():
    n=int(input())
    s=input()
    d={}
    for i in range(n):
        k=s[i:i+2]
        d[k]=d.get(k,0)+1
    r=max(d,key=lambda x:d[x])
    print(r)