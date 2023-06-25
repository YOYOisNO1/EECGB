    n = int(input())
    arr = map(lambda x: int(x) - 1, input().split())
    outs = set(arr)
    
    poss = True
    for i in range(n):
        if i not in outs:
            poss = False
    
def gcd(a, b):
        if b == 0: return a
        else: return gcd(b, a % b)
    
    if not poss:
        print(-1)
    else:
        lens = []
        v = set()
        for i in range(n):
            if i not in v:
                L = 1
                v.add(i)
                while arr[i] not in v:
                    i = arr[i]
                    v.add(i)
                    L += 1
                lens.append(L if L % 2 == 1 else L / 2)
        print(reduce(lambda) x, y: x * y / gcd(x, y), lens)