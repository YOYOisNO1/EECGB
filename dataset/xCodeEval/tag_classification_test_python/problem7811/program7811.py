    
def main():
        
        p1, t1 = readIntArr()
        p2, t2 = readIntArr()
        h, s = readIntArr()
        
        inf = int(4e18)
        dp = [inf] * (h + 5000)
        # dp[dmg] is the minimum time to achieve this damage given both fired at this same time
        dp[0] = 0
        
        for dmg in range(1, h + 5000):
            ta = t1
            tb = t2
            dmg2 = (p1 + p2 - s)
            while True:
                if dmg - dmg2 >= 0:
                    dp[dmg] = min(dp[dmg], max(ta, tb) + dp[dmg - dmg2])
                else:
                    break
                if ta + t1 < tb + t2:
                    ta += t1
                    dmg2 += (p1 - s)
                else:
                    tb += t2
                    dmg2 += (p2 - s)
                
        ans = inf
        for dmg in range(h + 5000):
            ta = tb = 0
            dmg2 = 0
            while dmg + dmg2 < h:
                if ta + t1 < tb + t2:
                    ta += t1
                    dmg2 += (p1 - s)
                else:
                    tb += t2
                    dmg2 += (p2 - s)
            ans = min(ans, dp[dmg] + max(ta, tb))
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
     
def queryInteractive(a, b):
        print('? {} {}'.format(a, b))
        sys.stdout.flush()
        return int(input())
     
def answerInteractive(ans):
        print('! {}'.format(ans))
        sys.stdout.flush()
     
    inf=float('inf')
    # MOD=10**9+7
    # MOD=998244353
     
    from math import gcd,floor,ceil
    import math
    # from math import floor,ceil # for Python2
     
    for _abc in range(1):
        main()