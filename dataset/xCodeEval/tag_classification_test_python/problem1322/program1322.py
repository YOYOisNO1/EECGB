    import math
    a,b = input().split()
    a,b = int(a),int(b)
    c = 10 ** b
    
def nod(a,b):
        if b==0:
            return a
        return int(nod(b, a%b))
    print(int(c*a/nod(c,a)))