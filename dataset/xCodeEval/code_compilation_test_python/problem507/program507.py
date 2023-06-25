def program507():
    #import math
    
    #n, m = input().split()
    #n = int (n)
    #m = int (m)
    #n, m, k = input().split()
    #n = int (n)
    #m = int (m)
    #k = int (k)
    n = int(input())
    #m = int(input())
    #s = input()
    #t = input()
    #h = list(map(int, input().split()))
    
    #print(l)
    #c = list(map(int, input().split()))
    
    #x1, y1, x2, y2 =map(int,input().split())
    #n = int(input())
    #f = []
    #t = [0]*n
    #f = [(int(s1[0]),s1[1]), (int(s2[0]),s2[1]), (int(s3[0]), s3[1])]
    #f = sorted (f, key = lambda tup: tup[0] )
    
    #h = [""] * n
    #f1 = sorted(f, key = lambda tup: tup[0])
    
    
    #f1 = sorted(t, key = lambda tup: tup[0])
    if (n == 0):
        print ("O-|-OOOO)"
    else:
        while(n > 0):
            a = n % 10
            if (a >= 5):
                s = "-O|"
                a -= 5
            else:
                s = "O-|"
            if (a == 0):
                s += "-OOOO"
            elif (a == 1):
                s += "O-OOO"
            elif (a == 2):
                s += "OO-OO"
            elif (a == 3):
                s += "OOO-O"
            elif (a == 4):
                s += "OOOO-"
            print(s)
            n //= 10
            
    