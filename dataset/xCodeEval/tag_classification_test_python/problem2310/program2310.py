def do():
        n = int(input())
        res = 0
        a,b = divmod(n, 100)
        n -= a * 100
        res += a
        a,b = divmod(n, 20)
        n -= a * 20
        res += a
        a,b = divmod(n, 10)
        n -= a * 10
        res += a
        a,b = divmod(n, 5)
        n -= a * 5
        res += a
        a,b = divmod(n, 1)
        n -= a * 1
        res += a
        print(res)
    
    do()
    
    
    
def templ():
        #input = sys.stdin.readline
        from pprint(import) pprint(#import) sys
        #sys.setrecursionlimit(100000)
    
    
        q = int(input())
        for _ in range(q):
            s = input()
            n = int(input())
            n, k = map(int, input().split())
            dat = list(map(int, input().split()))
    
    
        dat = [1, 2, 3]
        print(" ".join(list(map(str, res))))
    
        pass
        import math
        math.ceil(1.2)
        math.floor(1.2)
        round(1.2, 3)
    