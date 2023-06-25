    import itertools
    
def hash(cur):
        ret = []
        for _ in cur:
            #_.sort()
            ret.append(tuple(_))
        return tuple(ret)
    
def subsets(a,b,i=0,cur=[]):
        if i == len(a):
            #print cur,hash(cur)
            All.add(hash(cur))
            
        else:
            subsets(a,b,i+1,cur)
            subsets(a,b,i+1,cur+[[a[i],b[i]]])
            
        
def val(marry):
        ret = 0
        for mar in marry:
            ret += value[mar[0]][mar[1]]
        return ret
    
    #data = open("P6.txt")
    n,k,t = map(int,input().split())
    value = [[0]*n for z in range(n)]
    for _ in range(k):
        a,b,v = map(int,input().split())
        a -= 1
        b -= 1
        value[a][b] = v
        #value[b][a] = v
        
    All = set([])
    for per in itertools.permutations(range(n)):
        subsets(per,range(n))
    
    vals = []
    for _ in All: 
        #print _,val(_)
        vals.append(val(_))
    vals.sort()
    print(vals[t-1])