def program3530():
    from __future__ import print_function
    from __future__ import division
    try:
       input = input
    except NameError:
       pass
    k, a, b = [int(x) for x in input().split()]
    answer = a//k + b//k
    
    if answer <= 0 or (a//k < 1 and b//k < 1):
    	answer = -1
    elif a < k and b % k > 0:
    	answer = -1
    elif b < k and a % k > 0:
    	answer = -1
    print(answer)