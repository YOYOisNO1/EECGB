def program715():
    n, l, r = [int(i) for i in input().split(' ')]
    
    right = 2**r-1 + 2**(r-1)*(n-r)
    left = 2**l-1 + n-l
    
    print(left, right)