def program238():
    from sys import stdin,stdout
    y,bl=map(int,stdin.readline().split())
    a,b,c=map(int,stdin.readline().split())
    yr=a*2+b
    br=b*1+c*3
    c=0
    if yr >= y:
        c+=yr-y
    if br > bl:
        c+=br-bl
    stdout.write(str(c))