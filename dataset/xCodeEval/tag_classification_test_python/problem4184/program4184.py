def program4184():
    import sys
    import math
    input = sys.stdin.readline
    a,b,c=map(int,input().split())
    
    print(a*b+b*c+c*a-a-b-c+1)