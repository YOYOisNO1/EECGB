    import math
    module = 998244353
def is_prime(n):
        if n ==1:
            return True
        for x in range(2,int(math.sqrt(n)) +1):
            if n % x == 0:
                return False
        return True
    line1 = input().split(" ")
    n = int(line1[0])
    m = int(line1[1])
    arr =[]
    f = []
    arr.append(0)
    arr.append(1)
    for i in range(2,n+1):
        if is_prime(i):
            arr.append(i*arr[i-1])
        else:
            arr.append(arr[i-1])
    f.append(0)
    f.append(0)
    s = m
    ans = 0
    for i in range(2,n+1):
        tmp = (m * f[i-1]) % module
        x = m - int(m/arr[i])
        tmp += ((s-f[i-1])* x ) % module
        tmp %= module
        f.append(tmp)
        ans = (tmp + ans)% module
        s = (s*m)%module
    print(ans)