    n = input()
    a = input()
    a = a.split(' ')
    
def gcd(a,b):
        if b == 0:
            return a
        else:
            a1 = a%b;
            return gcd(b,a1);
    
    if n > 2:
        result = gcd(int(a[0]), int(a[1]))
        for i in range (2,n):
            result = gcd(result, int(a[i]));
        print(result) * n ;
    else:
        print(gcd(int(a[0]),) int(a[1])) * n;