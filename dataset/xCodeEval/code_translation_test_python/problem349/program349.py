def program349():
    [n,a,b,c,d]=[int(x) for x in input().split()]
    ma=max(abs(a+b-c-d),abs(a-d+c-b),abs(b-c+d-a),abs(c+d-a-b))
    if ma>n:
        print(0)
    else:
        print(n*(n-ma))