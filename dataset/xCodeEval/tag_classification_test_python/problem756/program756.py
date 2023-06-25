def program756():
    x,y,z=map(int, input().split())
    r=int((x*y*z)**0.5)
    print(4*(r/x+r/y+r/z))