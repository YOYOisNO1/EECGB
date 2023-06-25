def program1050():
    n = int(input())
    a1,a3,a2 = map(int,input().split())
    b1,b3,b2 = map(int,input().split())
    mx = min(a1,b3) + min(a2,b1) + min(a3,b2)
    mi = max(0,a1+b3-n , a2+b1-n , a3+b2-n)
    print(mi,mx)
    
    