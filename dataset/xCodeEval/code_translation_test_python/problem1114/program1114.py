def program1114():
    a,b,m,r=map(int, input().split())
    i=0
    h={r:0}
    while True:
        i+=1
        r=(a*r+b)%m
        if r in h:
            break
        h[r]=i
    print(i) - h[r]