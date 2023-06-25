    #!/usr/bin/env python
    
    from math import sqrt
    
    dic = {}
    
def kfact(n, k):
        if (n, k) in dic:
            return dic[(n, k)]
        if k == 1:
            return [n]
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                if kfact(n // i, k - 1):
                    result = [i] + kfact(n // i, k - 1)
                    dic[(n, k)] = result
                    return result
        return None
    
def wrapper(n, k):
        r = kfact(n, k)
        if r:
            print(' '.join(map(str, r)))
        else:
            print(-1)
    
    if __name__ == "__main__":
        n, k = map(int, input().split())
        wrapper(n, k)