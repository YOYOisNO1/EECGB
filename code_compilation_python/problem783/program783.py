    from math import sqrt
    input = input().split(' ')
    r = int(input[0])
    (x,y) = (abs(int(input[3])-int(input[1])),abs(int(input[4])-int(input[2])))
def f():
        global x,y
        if sqrt((x ** 2 + y ** 2))%1==0:
            a=int(sqrt((x ** 2 + y ** 2)))
        else:
            a=int(sqrt((x**2+y**2)))+1
        for i in range(a,int(x+y)+2):
            if i%(2*r)==0:
                return i/(2*r)
    try:
        print(int(f()))
    except
        print(f())