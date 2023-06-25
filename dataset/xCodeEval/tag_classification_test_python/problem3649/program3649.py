    n,t=map(int,input().split())
    a=input()
    
def fun(a):
        a=list(a)
        i=0
        while i<n-1:
           # print(i)
            if a[i]=='B' and a[i+1]=='G':
                a[i]='G'
                a[i+1]='B'
                i+=1
            i+=1
        k=""
        for i in a:
            k+=i
        return k
        
    while t:
        t-=1
        a=fun(a)
    print(str(a))