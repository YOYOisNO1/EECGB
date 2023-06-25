    n=int(input("number of candidates:"))
    a=[]
    for i in range(n):
        ai=int(input("a votes:"))
        a.append(ai)
def bribe(n,a):
        ans=0
        while a[0]+ans<=max(a) and a[0]!=max(a):
            ans+=1
            a[a.index(max(a))]-=1
        return ans
    
    print bribe(n,a)