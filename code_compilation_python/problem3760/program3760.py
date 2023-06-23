    """
    NTC here
    """
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**7)
    
    
def iin(): return int(stdin.readline())
     
     
def lin(): return list(map(int, stdin.readline().split()))
    
    
    # range = xrange
    # input = input
    
def bcheck(a,l,r):
        if a[l]==a[r]:return -1
        a1=a[:]
        a1[l],a1[r]=a1[r],a1[l]
        N=len(a)
        p,n=[],[]
        for i in range(N):
            if a1[i]==')':
                if p:
                    p.pop()
                else:
                    n.append(i)
            else:
                p.append(i)
        l=len(p)
        rt=0
        if l>0:
            rt=n[-1]+1
        if rt:
            a1=a1[rt:]+a1[:rt]
        ch,pt=0,0
        for i in a1:
            if i=='(':
                pt+=1
            else:
                pt-=1
            if pt==0:ch+=1
        #print(a1,ch)
        
        return ch
    
def main():
        N=iin()
        a=list(input())
        c1,c2=a.count(')'),a.count('(')
        if c1!=c2 or N%2:
            print(0)
            print(1,1)
        else:
            mx=[-1,0,0]
         #   print(a)
            for i in range(N):
                for j in range(i+1,N):
                    if a[i]!=a[j]:
                        val=bcheck(a,i,j)
                        if mx[0]<val:
                            mx=[val,i,j]
          #  print(a)
            print(mx[0])
            print(mx[1]+1,mx[2]+1)
    
                    
    
                
    
    
    
    
    
    
    
    
    main()
    # try:
    #     main()
    # except Exception as e: print(e)