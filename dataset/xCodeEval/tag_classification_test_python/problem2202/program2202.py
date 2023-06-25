def program2202():
    from sys import stdin
    
    inp = stdin.readline
    
    a, b, s = [int(x) for x in inp().strip().split()]
    
    if (a+b)%2 == s%2 and s>=abs(a)+abs(b):
        print("YES")
    else:
        print("NO")