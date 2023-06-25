    n, x, pos = [int(a) for a in input().split()]
    
def fac(n):
        return 1 if n<=1 else fac(n-1)*n
    
    mod = int(1e9+7)
    
    count_left = 0
    count_right = 0
    
def binary_search(a, x):
        global count_left, count_right
        left =  0
        right = len(a)
        while left < right:
            middle = (left + right) // 2
            # print(middle)
            # if a[middle] == x:
                # break
            if a[middle] <= x:
                left = middle + 1
                if a[middle] != x:
                    count_left += 1
            else:
                right = middle
                count_right += 1
    
    nums = list(range(n))
    binary_search(nums, pos)
    # print(count_left, count_right)
    
    
    if x <= count_left or x > n-count_right:
        print(0)
        import sys
        sys.exit()
    
def binomial(n, k):
        return 1 if n <= 0 else fac(n) // fac(n-k)
    
    left = max(1, (binomial(x - 1, count_left)) % mod)
    right = max(1, (binomial(n - x, count_right)) % mod)
    print((fac(n - count_left - count_right - 1) * left * right) % mod)