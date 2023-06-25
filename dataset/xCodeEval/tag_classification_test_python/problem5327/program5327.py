    
def naiveSolve():
        
        
        
        return
    
    
    
def solve():
        
        
        
        return
    
    import __pypy__
    int_add = __pypy__.intop.int_add
    int_sub = __pypy__.intop.int_sub
    int_mul = __pypy__.intop.int_mul
def make_mod_mul(mod = 10**9 + 7):
        fmod_inv = 1.0 / mod
    def mod_mul(a, b, c=0):
            res = int_sub(
                int_add(int_mul(a, b), c),
                int_mul(mod, int(fmod_inv * a * b + fmod_inv * c)),
            )
            if res >= mod:
                return res - mod
            elif res < 0:
                return res + mod
            else:
                return res
        return mod_mul
    
    
def main():
        
        n,MOD=readIntArr()
        
        mod_mul=make_mod_mul(MOD)
        
        dp=[0]*(n+5)
        dp[1]=1
        prefixSum=1
        for i in range(2,n+1):
            dp[i]+=prefixSum
            # print('i:{} pfx:{}'.format(i,prefixSum))
            # sqRtI=pow(i,0.5)
            z=2
            visitedDivisors=set()
            while z*z<=i:
                dp[i]+=dp[i//z]
                dp[i]%=MOD
                visitedDivisors.add(i//z)
                # print('i:{} z:{} i//z:{}'.format(i,z,i//z))
                z+=1
            c=1
            # while c*c<i:
            while c*c<i and c not in visitedDivisors:
                zLeft=floor(i/(c+1)+1)
                zRight=floor(i/c)
                cnts=zRight-zLeft+1
                toAdd=mod_mul(dp[c],cnts)
                dp[i]+=toAdd
                dp[i]%=MOD
                # print('i:{} c:{} zLeft:{} zRight:{} cnts:{}'.format(i,c,zLeft,zRight,cnts))
                c+=1
            prefixSum+=dp[i]
            prefixSum%=MOD
        ans=dp[n]
        # print(dp)
        print(ans)
        
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
    # MOD=10**9+7
    MOD=998244353
    
    from math import gcd,floor,ceil
    # from math import floor,ceil # for Python2
     
    for _abc in range(1):
        main()