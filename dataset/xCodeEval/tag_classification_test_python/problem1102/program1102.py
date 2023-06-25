def program1102():
    import math
    import sys
    
    
    n = int(input())
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))
    
    mn = 0
    
    for i in range(3):
        sum = 0
        
        for j in range(3):
            if j == (i+1) % 3:
                continue
            sum += br[j]
        mn = max(mn, max(ar[i]-sum, 0) )
    
    mx = 0
    for i in range(3):
        mx += min(ar[i], br[ (i+1) % 3 ])
    
    print(mn, mx)