def program1154():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    
    res = 0
    if(f>e):
        res = min(b,c,d)*f + min(a,d-min(b,c,d))*e
    else:
        res = min(a,d)*e + min(b,c,d-min(a,d))*f
    print(res)