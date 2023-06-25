    import math
def printSubsequences(arr, n,a) : 
        c=0
        opsize = math.pow(2, n) 
        for counter in range( 1, (int)(opsize)) : 
            ans=0
            for j in range(0, n) : 
                if (counter & (1<<j)) : 
                    ans+=arr[j]
            if ans==a:
                c+=1
        return c        
        
    # Driver program 
    n=int(input())
    l=[]
    s=0
    for i in range(0,n):
        a=int(input())
        l.append(a)
        s+=a
    if n==1: 
        if s!=360:
            print("NO")
        else:
            print("YES")
    elif s%360 == 0:
        print("YES")
    else:
        if s%2 != 0:
            print("NO")
        else:
            a=(s)//2
            if s<360:
                d=printSubsequences(l,n,a)
                if d>0:
                    print("YES")
                else:
                    print("NO")
            else:
                d=printSubsequences(l,n,a)
                if d>0:
                    print("YES")
                else:
                    a=(s-360)//2
                    d=printSubsequences(l, n,a)
                    if(d>0):
                        print("YES")
                    else:
                        print("NO")
        