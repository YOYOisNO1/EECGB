def program6009():
    import sys
    input=sys.stdin.readline
    from collections import deque
    
    n=int(input())
    c=2*3*4*pow(4,n-3)
    
    for i in range(0,n-3):
        c+=4*3*3*(pow(4,i)*pow(4,n-i-4))
    print(max(c,1))    