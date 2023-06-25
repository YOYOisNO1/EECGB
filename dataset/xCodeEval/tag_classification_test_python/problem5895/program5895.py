def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
def lcm(num1, num2):
        return num1 * num2 /  gcd ( num1 , num2 )
    
def lcm_arr(arr):
        if len(arr) == 1:
            return arr[0]
        ans = lcm(arr[0], arr[1])
        for a in arr[1:]:
            ans = lcm(ans, a)
        return ans
    
    n = int(input())
    cr = map(int, input().split())
    
    l = []
    vs = set()
    for i in range(1, n+1):
        if i in vs:
            continue
        nv = i
        c = 0
        while nv not in vs:
            vs.add(nv)
            nv = cr[nv - 1]
            c+=1
        if nv != i:
            print(-1)
            exit()
        if c %2 == 0:
            l.append(c / 2)
        else:
            l.append(c)
    
    print(lcm_arr(l))