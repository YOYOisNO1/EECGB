    
def naiveSolve(n,k):
        
        ans=[0]
    def dfs(i):
            if i==n:
                x=(1<<k)-1
                y=0
                for v in arr:
                    x&=v
                    y^=v
                if x>=y:
                    ans[0]+=1
                    # print(bin(arr[0]),bin(arr[1])) ##
                return
            for mask in range(1<<k):
                arr[i]=mask
                dfs(i+1)
        arr=[-1]*n
        dfs(0)
        return ans[0]
        
        return
    
    m=(200005)
    
    MOD=10**9+7
    MAX=m
    fact=[1]
    for zz in range(1,MAX+1):
        fact.append(((fact[-1]%MOD)*zz%MOD)%MOD) #with MOD
    #    fact.append(fact[-1]*zz) #without MOD
def nCr(n,r): #choose, MOD is prime
        num=fact[n]
        den=((fact[r]%MOD)*(fact[n-r]%MOD))%MOD #with MOD
        return ((num%MOD)*pow(den,MOD-2,MOD))%MOD #with MOD
    #    den= fact[r]*fact[n-r]# without MOD
    #    return num//den # without MOD
    
    
    
def main():
        
        t=int(input())
        allans=[]
        for _ in range(t):
            n,k=readIntArr()
            # k is the number of bits
            
            # solve for 1 bit first
            largerCnts=0
            drawCnts=0
            # if oneXor[n]==1: # all 1s
            if n%2==1: # all 1s will give all number of 1s which gives xor of 1
                drawCnts+=1
            else:
                largerCnts+=1
            # for ones in range(n):
            #     zeroes=n-ones
            #     if oneXor[ones]^zeroXor[zeroes]==0:
            #         drawCnts+=nCr(n,ones)
            #         drawCnts%=MOD
            for ones in range(0,n,2): # even number of ones to get xor of 0
                drawCnts+=nCr(n,ones)
                drawCnts%=MOD
            
            # Iterate for each bit
            # ... draw draw larger any any...
            suffixMultiplier=[1]*(k+2) # suffix is unrestricted
            mul=pow(2,n,MOD)
            for i in range(k,-1,-1):
                suffixMultiplier[i]=(suffixMultiplier[i+1]*mul)%MOD
            
            ans=0
            prefixMultiplier=1 # associated with draws
            for draws in range(k): # iterate for each bit
                ans+=prefixMultiplier*largerCnts*suffixMultiplier[draws+2]
                prefixMultiplier=(prefixMultiplier*drawCnts)%MOD
            ans+=prefixMultiplier # all draws
            ans%=MOD
            allans.append(ans)
            
            # print('ans:{} naive:{}'.format(ans,naiveSolve(n,k)))
            
        multiLineArrayPrint(allans)
        
        return
    
    
    
    import sys
    input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
    # input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
    
def oneLineArrayPrint(arr):
        print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
        print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
        print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
     
def readIntArr():
        return [int(x) for x in input().split()]
# def readFloatArr():
    #     return [float(x) for x in input().split()]
     
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
        dv=defaultValFactory;da=dimensionArr
        if len(da)==1:return [dv() for _ in range(da[0])]
        else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
     
def queryInteractive(x):
        print('{}'.format(x))
        sys.stdout.flush()
        return int(input())
     
def answerInteractive(ans):
        print('! {}'.format(ans))
        sys.stdout.flush()
     
    inf=float('inf')
    MOD=10**9+7
    # MOD=998244353
    
    from math import gcd,floor,ceil
    # from math import floor,ceil # for Python2
     
    for _abc in range(1):
        main()