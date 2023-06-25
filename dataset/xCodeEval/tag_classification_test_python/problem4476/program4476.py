def program4476():
    
    mod=10**9+7
    import math
    for _ in range(1):
        n,m=map(int,input().split())
        s=input()
        arr=[0 for i in range(26)]
        for i in s:
            arr[ord(i)-97]=1
        i=0
        ans=0
        while(i<26 and m>0):
            if(arr[i]==1):
                ans+=(i+1)
                i+=1
                m-=1
            i+=1
        if(m==0):
            print(ans)
        else:
            print(-1)
            #print(m)
        
        
    
    