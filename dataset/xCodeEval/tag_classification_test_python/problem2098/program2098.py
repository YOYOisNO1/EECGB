def program2098():
    
    import sys
    import math as mt
    #input=sys.stdin.buffer.readline
    #import bisect
    mod=1000000007
    #t=int(input())
    #tot=0
    t=1
    
    for __ in range(t):
        #n=int(input())   
        n,k,d=map(int,input().split())
        ans=0
        cnt=[]
        for i in range(1,k+1):
            cnt.append(i)
        cnt1=[]
        for i in range(1,d):
            cnt1.append(i)
            
        ways=[0]*(n+1)
        ways[0]=1
        for i in range(1,n+1):
            for j in range(len(cnt)):
                if cnt[j]<=i:
                    ways[i]=(ways[i]%mod+ways[i-cnt[j]]%mod)%mod
                    
        ways1=[0]*(n+1)
        #print(ways,cnt)
        
        ways1[0]=1
        for i in range(1,n+1):
            for j in range(len(cnt1)):
                if cnt1[j]<=i:
                    ways1[i]=(ways1[i]%mod+ways1[i-cnt1[j]]%mod)%mod
        #print(ways1,cnt1)            
        print((ways[n]-ways1[n])%mod)    
        
                   
                
                
            
            