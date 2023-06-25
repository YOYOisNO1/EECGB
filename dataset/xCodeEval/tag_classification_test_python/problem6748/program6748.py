    import sys
    sys.setrecursionlimit(100000)
def help(n,k):
        while(True):
            if k>lent[n]:
                return '.'
            elif n==0:
                return arr[k-1]
            elif k<=a:
                return str1[k-1]
            elif a<k<=a+lent[n-1]:
                n,k=n-1,k-a
                continue
            elif a+lent[n-1]<k<=a+lent[n-1]+b:
                return str2[k-1-a-lent[n-1]]
            elif a+lent[n-1]+b<k<=a+b+2*lent[n-1]:
                n,k=n-1,k-a-b-lent[n-1]
                continue
            elif a+b+2*lent[n-1]<k<=lent[n]:
                return str3[k-1-a-b-2*lent[n-1]]
    
    
    q=input()
    n=[0]*q
    k=[0]*q
    for i in range(q):
        n[i],k[i]=map(int,input().split())
    n_max=max(n)
    
    arr=list('What are you doing at the end of the world? Are you busy? Will you save us?')
    
    lent=[0]*(n_max+1)
    str1=list('What are you doing while sending "')
    str2=list('"? Are you busy? Will you send "')
    str3=list('"?')
    
    a,b,c=len(str1),len(str2),len(str3)
    lent[0]=len(arr)
    for i in range(1,n_max+1):
        lent[i]=min(2*(10**18),2*lent[i-1]+a+b+c)
    
    ans=[]
    for i in range(q):
        x,y=n[i],k[i]
        ans.append(help(x,y))
    print('').join(ans)