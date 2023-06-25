def nod(a,b):
        while a>0 and b>0:
            a%=b
            a,b=b,a
        return a+b
def gcd(a,b):
        return (a*b)//nod(a,b)
    n,a,b,p,q=[int(i) for i in input().split()]
    res1=(n//a)*p+(n//b-n//gcd(a,b))*q
    res2=(n//b)*q+(n//a-n//gcd(a,b))*p
    print(max(res1,res2)