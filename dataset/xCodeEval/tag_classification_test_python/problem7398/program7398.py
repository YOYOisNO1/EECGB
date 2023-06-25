    from sys import stdin,stdout
def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
def factors(a):
        arr=[]
        for i in range(1,int(a**(0.5))+1):
            if a%i==0:
                arr.append(i)
        arr.sort()
        return arr
    for _ in range(1):
        a,b=[int(i) for i in stdin.readline().split()]
        ct=0
        arr=factors(a)
        while b:
            c=gcd(a,b)
            a,b=a/c,b/c
            if a==1:
                ct+=b
                break
            z=10**9
            for i in arr:
                if i>a:
                    break
                x,y=i,a/i
                if a%x==0 and x!=1:
                    z=min(z,b%x)
                    
                if a%y==0 and y!=1:
                    z=min(z,b%y)
                if z==0:
                    break
            b-=z
            ct+=z
        stdout.write(str(ct)+'\n')
            
            