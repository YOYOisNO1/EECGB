    import sys
    
    sys.setrecursionlimit(5000)
def help(x):
        if x==1:
            return 0
        else:
            a=1
            b=2
            ans=0
            while(b<=x):
                ans=ans+a*(x/b)
                b*=2
                a*=2
            return ans
def hel(n):
        #print(n)
        if n==1:
            return 0
        for i in ps:
            if i == n:
                return help(n)
            elif i>n:
                rem=n-i/2
                num=i/2
                #print(help(num),hel(rem),num)
                return help(num)+hel(rem)+num
    
    
    
    
    
    n=input()
    ps=[]
    i=2
    while(i<10**13+5):
        ps.append(i)
        i=i*2
    #print(ps)
    ans=hel(n)
    print(ans)
    
    
    
    
    