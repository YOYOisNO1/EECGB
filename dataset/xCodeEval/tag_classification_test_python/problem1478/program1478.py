def countMaxSetBits(left, right):
        while (left | (left + 1)) <= right:
            left |= left + 1
        return left
    
    
    # n=int(input())
    # n,k=map(int,input().split())
    # arr=list(map(int,input().split()))
    #ls=list(map(int,input().split()))
    #for i in range(m):
    # for _ in range(int(input())):
    #from collections import Counter
    #from fractions import Fraction
    #s=iter(input())
    #from collections import deque
    #for _ in range(int(input())):
    #n,k=map(int,input().split())
    #arr=list(map(int,input().split()))
    
    n=int(input())
    var=n%4
    if n==0:
        print(1)
        exit()
    if var==0:
        print(6)
    if var==1:
        print(8)
    if var==2:
        print(4)
    if var==3:
        print(2)