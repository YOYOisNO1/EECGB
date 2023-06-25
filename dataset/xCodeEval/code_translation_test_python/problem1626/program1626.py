def naiveSolve():
        
        
        
        return
    
    
    
def solve():
        
        
        
        return
    
def getP(n,x):
        # calculate for all 3 known
        if x<3:
            p3=0
        else:
            p3=(x/n)*((x-1)/(n-1))*((x-2)/(n-2))
        
        # calculate for 2 known
        if x<2:
            p2=0
        else:
            p2=3*(x/n)*((x-1)/(n-1))*((n-x)/(n-2))
            # discard the unknown
        
        # calculate for 1 known
        if x<1:
            p1=0
        else:
            p1=3*(x/n)*((n-x)/(n-1))*((n-x-1)/(n-2))
            
            p11=p1*(1/3)*0.5 # opponent picks the same 0 map as Johnny to discard
            p12=p1*(1/3) # opponent picks a different 0 map as Johnny to discard
            p1=p11+p12
            
        return p1+p2+p3
    
# def getP2(n,x):
    #     from random import randint
    #     arr=[0]*(n-x)+[1]*n
    #     cnts=100000
    #     succeedCnts=0
    #     for _ in range(cnts):
    #         a=b=c=randint(0,n-1)
    #         while b==a:
    #             b=randint(0,n-1)
    #         while c==a or c==b:
    #             c=randint(0,n-1)
    #         arr3=[arr[a],arr[b],arr[c]]
    #         x=sum(arr3) # known map cnts
    #         y=3-x
    #         opponentPick=randint(0,2)
    #         if y>0:
    #             myPick=-1
    #             while myPick==-1 or arr3[myPick]==1:
    #                 myPick=randint(0,2)
    #         else:
    #             myPick=randint(0,2)
    #         arr2=[]
    #         for i in range(3):
    #             if i!=opponentPick and i!=myPick:
    #                 arr2.append(arr3[i])
    #         succeedCnts+=arr2[randint(0,len(arr2)-1)]
    #     return succeedCnts/cnts
        
    
def main():
        
        eps=0
        
        n,p=input().split()
        n=int(n)
        p=float(p)
        
        x=-1
        bb=n
        while bb>0:
            while x+bb<=n and getP(n,x+bb)+eps<p:
                x+=bb
            bb//=2
        x+=1
        
        print(x)
        
        # for x in range(0,n+1):
        #     p=getP(n,x)
        #     p2=getP2(n,x)
        #     print('x:{} p:{} p2:{}'.format(x,p,p2))
        
        return
    
    
    import sys
    # input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
    input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
    
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
    # MOD=998244353
    
    from math import gcd,floor,ceil
    # from math import floor,ceil # for Python2
     
    for _abc in range(1):
        main()