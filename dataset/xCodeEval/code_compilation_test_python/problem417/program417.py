    mo = 998244353
    
def ge(n):
        a = [0] * (n + 5)
        a[1] = 1
        a[2] = 1
        for i in range(3, n + 1):
            a[i] = a[i - 1] + a[i - 2]
            a[i] %= mo
        return a[n]
    
def min_y(b, n):
      #  print (b, n)
        if (n == 1):
            return b
        if (n % 2 == 0):
            return min_y(b * b % mo, n // 2) % mo
        return b * min_y(b % mo, n - 1) % mo
    
    n = int(input())
    get_n = ge(n)
    ans = 2
    st = n * (mo - 2)
    while (st != 1):
        if (st % 2 == 0):
            ans = ans * ans % mo
            st //= 2
        else:
            ans = ans % mo
            st -= 1
    
    print(get_n * ans % mo)