    c=1000000007
    
    #special cases for k=0, 1
    
    p, k = map(int, input().split(" "))
    
"""def binary(number):
        #turn into string
        s=""
        while number!=0:
            r = number%2
            s = str(r) + s
            number = number//2
        return s
    
def mod(base, expo, mod):
        #write expo as binary and calculate to the power of 2 power
        ans=1
        s=binary(expo)
        l=len(s)
        #calculate a list of remainders of length l
        mods = []
        current=base
        for i in range (l):
            mods = [current] + mods
            current = (current**2) % mod
        #print(mods, s)
        for i in range (l):
            if s[i] == "1":
                ans *= mods[i]
                #print(ans)
                ans = ans%mod
        return ans
    """
    if k==0:
        answer=pow(p, p-1, c)
    elif k==1:
        answer=pow(p, p, c)
    else:
        #counted = [False] * (p-1)
        size = 1
    
    """def modify(init):
            global counted
            new=init*k
            new = new%p
            counted[init-1]=True
            while new!=init:
                #print(new)
                counted[new-1]=True
                new=new*k
                new = new%p
                #print(new)
    
        for j in range (p-1):
            if counted[j]==False:
                i=j+1
                #print("i", i)
                modify(i)
                #print(counted)
                cycles+=1
        """
        new=k
    
        while new!=1:
            size+=1
            new*=k
            new=new%p
    
        cycles = (p-1)//size
        
        #print(cycles)
        answer=pow(p, cycles, c)
    
    #too slow, issue is not with mod
    #fuck python and fuck c++ dont have time to recode this in c++ why can't python be faster
    
    print(answer)