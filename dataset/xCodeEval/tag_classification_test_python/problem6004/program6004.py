def program6004():
    n=input()
    a=map(int,input().split())
    b=sorted(a)
    f={}
    for i in range(n):
    	f[b[i]]=i
    for x in a:
    	print(b[(f[x]+1)%n],)