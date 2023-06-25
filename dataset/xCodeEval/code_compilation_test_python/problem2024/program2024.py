def program2024():
    from math import sqrt
    from sys import stdin
    input = stdin.readline
     
    n, k = [int(i) for i in input().split()]
     
    
    print(((3+2*n)-sqrt((3+2*n)**2-4*(n**2+n-2k)))/2)