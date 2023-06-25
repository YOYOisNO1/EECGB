def program1905():
    x,y = map(int,input().split())
    if(x>0 and y>0):
        print(0,x+y,x+y,0)
    elif(x>0 and y<0):
        print(0,-1*(x+abs(y)),x+abs(y),0)
    elif(x<0 and y>0):
        print(-1*(y+abs(x)),0,0,y+abs(x))
    else:
        z = x+y
        print(z,0,0,z)