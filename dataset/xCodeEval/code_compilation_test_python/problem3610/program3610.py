def pall(n):
        if str(n)==str(n)[::-1]:
            return True
        else:
            return False    
def sieve(n):  
        p = 2
        while (p * p <= n):  
            if (prime[p] == True):  
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
    n=10**5        
    prime = [True for i in range(n+1)]
    nopr=[0]*(n+1)
    pallin=[0]*(n+1)
    sieve(n)
    prime[1]=False
    for i in range(2,n+1):
        if prime[i]:
            nopr[i]=nopr[i-1]+1
        else:
            nopr[i]=nopr[i-1]
    for i in range(1,n):
        if pall(i):
            pallin[i]=pallin[i-1]+1
        else:
            pallin[i]=pallin[i-1]    
    p,q = map(int,input().split())
    #print(pallin[:100],nopr[:100])
    for i in range(n,0,-1):
    #    print(nopr[i],pallin[i],nopr[i]*q,pallin[i]*p)
        if q*(nopr[i])<=p*(pallin[i]):
            print(i)
            exit()    
    print("Palindromic tree is better than splay tree")