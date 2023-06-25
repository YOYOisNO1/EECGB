    mod=1000000007
def sol(n,k):
        arr=[0 for i in range(n+1)]
        acum=[0 for i in range(n+1)]
        for i in range(1,min(k,n)+1):
                arr[i]=1
                acum[i]=1
        for qq in range(n):
            arr1=[0 for i in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,k+1):
                    if arr[i]!=0 and i+j<len(arr1):
                        arr1[i+j]=(arr1[i+j]+arr[i])%mod
            for i in range(n+1):
                acum[i]=(acum[i]+arr1[i])%mod
            arr=arr1.copy()
        return(acum[-1])
    
                
            
            
    from sys import stdin
    n,k,d=map(int,stdin.readline().strip().split())
    print((sol(n,k)-sol(n,d-1))%mod)