def program957():
    n = int(input())
    #rock scissors paper
    a1,a2,a3 = map(int,input().split())
    b1,b2,b3 = map(int,input().split())
    maximum = min(a1,b2) + min(a2,b3) + min(a3,b1)
    minimum = min(a1,b1+b3) + min(a2,b2+b1) + min(a3,b3+b2)
    print(n-minimum,maximum)