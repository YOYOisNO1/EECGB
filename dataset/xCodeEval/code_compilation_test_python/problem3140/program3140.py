    n=input()
def isprime(n):
        for i in range(2,int(n**.5)+1):
            if n%i==0: return 0
        return 1
    l=[]
    for i in range(2,1300):
        if(isprime(i)==1):l.append(i)
    ind=0
    if n!=1 print n
    while n>1 and l[ind]*l[ind]<=n:
        if(n%l[ind]==0):
            n/=l[ind]
            print n
        else: ind+=1
    print 1
        