def program536():
    a,b,c = input()
    x =a+c-b
    y = a+c-b
    z = c+b-a
    if (x >= 0) && (x%2 == 0)&& (y >= 0) && (y%2 == 0)&&(z >= 0) && (z%2 == 0):
        print(x/2,y/2,z/2)
    else:
        print("Impossible")