def f(a,b):
        for i in range(min(b-1,a),0,-1):
            if not a%i:
                return i
    
def f1(a,b,c):
        return a*b//c
    
    n,k = map(int, input().split())
    c = f(n,k)
    print(f1(n,k,c)+c)