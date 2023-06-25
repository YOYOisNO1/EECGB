def program7197():
    a = map(int, input().strip().split())
    b = map(int, input().strip().split())
    c = map(int, input().strip().split())
    
    vect=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    
    if vect == 0:
        print("TOWARDS")
    elif vect < 0:
        print("RIGHT")
    else:
        print("LEFT")