def program3079():
    from math import ceil
    n = int(input())
    xs = list(map(int, input().split()))
    ret = 1
    xs.sort()
    for i in range(n):
      ret = max(ret, int(ceil((i+1)/(xs[i]+1))))
    
    print(ret)