def program3718():
    a,ta = list(map(int, input().strip().split()))
    b,tb = list(map(int, input().strip().split()))
    s = str(input())
    
    ha = int(s[0:2])
    ma = int(s[3:5])
    
    l = []
    
    lb = ha * 60 + ma
    ub = lb + ta
    
    start = 300
    
    c = 0
    while start < 24*60:
        if max(lb, start) < min(ub, start + tb):
            c += 1
        start += b
    print(c)