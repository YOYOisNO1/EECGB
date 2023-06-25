def program2530():
    a,b,c=sorted(10*ord(y)+int(x)for x,y in input().split())
    s={b-a,c-b}
    print(2-bool(s&{0,1,2})-(s in({0},{1})))