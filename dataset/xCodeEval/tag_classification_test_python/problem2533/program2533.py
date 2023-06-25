def program2533():
    #import math
    #n, m = input().split()
    #n = int (n)
    #m = int (m)
    #k = int (k)
    s1, s2, s3 = input().split()
    #x = int(input())
    
    #h = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    #c = list(map(int, input().split()))
    
    #x1, y1, x2, y2 =map(int,input().split())
    #n = int(input())
    #f = []
    #f = [0]*n
    #t = [0]*n
    f = [(int(s1[0]),s1[1]), (int(s2[0]),s2[1]), (int(s3[0]), s3[1])]
    f = sorted (f, key = lambda tup: tup[0] )
    
    #h = [""] * n
    #f1 = sorted(f, key = lambda tup: tup[0])
    
    #f1 = sorted(t, key = lambda tup: tup[0])
    m = 2
    if (s1 == s2 and s2 == s3):
        m = 0
    
    elif (f[0][0] == f[1][0]-1 and f[1][0] == f[2][0]-1 and s1[1] == s2[1] and s2[1] == s3[1]):
        m = 0
    elif ((f[0][1] == f[1][1] and f[0][0] == f[1][0]-1) or (f[0][1] == f[2][1] and f[0][0] == f[2][0]-1) or (f[0][1] == f[1][1] and f[0][0] == f[1][0]-2) or (f[1][1] == f[2][1] and f[1][0] == f[2][0]-2) or (f[0][1] == f[2][1] and f[0][0] == f[2][0]-2) or (f[1][1] == f[2][1] and f[1][0] == f[2][0]-1) or s1 == s2 or s2 == s3 or s1 == s3):
        m = 1
        
    print(m)