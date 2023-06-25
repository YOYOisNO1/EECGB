def program281():
    N = int(input())
    Arr = input().split(' ')
    
    for i in xrange(len(Arr)):
        if int(Arr[i]) == 1: a = i
        elif int(Arr[i]) == N: b = i
    
    print(abs(a-b)) + max(min(a,b), N - max(a,b) - 1)