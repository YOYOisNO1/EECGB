    from fractions import gcd
    n=input()
    a=[0]+map(int,input().split())
    parent = [i for i in range(n+1)]
    freq = [0]*(n+1)
    
def find(x):
        if parent[x]==x:return x
        parent[x] = find(parent[x])
        return parent[x]
    
def unite(x, y):
        parent[find(x)] = find(y)
    
    ans=1
    for i in range(1, n+1):
        freq[a[i]]+=1
        if freq[a[i]] > 1:
            print(-1)
            exit(0)
        unite(i, a[i])
    sizes={}
    for i in range(1, n+1):
        x=find(i)
        if x in sizes:sizes[x]+=1
        else:sizes[x]=1
    a=[]
    for x in sizes:
        if sizes[x]&1:a.append(sizes[x])
        else:a.append(sizes[x]/2)
    
def lcm(a,b):
        return a*b/gcd(a,b)
def lcmm(*args):
        return reduce(lcm,args)
    
    print(lcmm(*a))