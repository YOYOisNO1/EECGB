def program103():
    from itertools import product
    lucky = []
    
    l,r = input().split()
    lw, rw = len(l), len(r)
    l, r = int(l), int(r)
    
    for i in range(lw,rw+1):
        lucky+=[int(''.join([str(y) for y in x])) for x in list(product([4,7],repeat=i))]
    lucky+=[int('4'*(rw+1))]
    ans=0
    for i in range(l,r+1):
        j=0
        while lucky[j]<i:
            j+=1
        ans+=lucky[j]
    print(ans)