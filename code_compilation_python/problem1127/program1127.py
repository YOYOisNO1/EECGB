    import math
def divisors(n):
        i=2
        l=[]
        while i <= math.sqrt(n):
            if n%i==0:
                if n/i==i:
                    l.append(i)
                else:
                    l.append(i)
                    l.append(n//i)
            i=i+1
        return l
def pebbles(n):
        if n==1:
            return 1
        else:
            c=divisors(n)
            m=len(c)
            result=[]
            for i in range(0,m):
                result.append(pebbles(n//c[i])
            return(n+max(result))
    n=int(input())
    print(pebbles(n))
        
        