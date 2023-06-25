def program747():
    c, v0, v1, a, l =map(int,input().split())
    d=v0
    n=1
    current_speed=v0
    while d<c:
        temp=current_speed+a
        if temp>=v1:
            current_speed=v1
        else:
            current_speed=temp
        d+=(current_speed-l)
        n+=1
    print(n)