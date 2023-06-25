    n = int(input())
    arr = list(map(int,input().split()))
    odds = evens = 0
    for a in arr:
        if a!=0:
            odds += a%2
            evens += a%2==0
    
        
def parity(i, e, o, last=None):
        if i==n: return 0  
        elif arr[i]==0 and last==None:
            even = parity(i+1,e-1,o,0) if e>0 else float('inf')
            odd = parity(i+1,e,o-1,1) if o>0 else float('inf')
            return min( even, odd )
        elif last==None:
            return parity(i+1,e,o,arr[i]%2)
        elif arr[i]!=0:
            if arr[i]%2 != last: return 1 + parity(i+1,e,o,arr[i]%2)
            else: return parity(i+1,e,o,last)
        else:
            if last==1:
                if o!=0 and e!=0: return min( 1+parity(i+1,e-1,o,0), parity(i+1,e,o-1,1) )
                elif o==0: return 1+parity(i+1,e-1,o,0)
                else: return parity(i+1,e,o-1,1)
            else:
                if o!=0 and e!=0: return min(1+parity(i+1,e,o-1,1), parity(i+1,e-1,o,0))
                if e==0: return 1+parity(i+1,e,o-1,1)
                else: return parity(i+1,e-1,o,0)
            
    print(parity(0,n//2-evens,(n+1)//2-odds))