def program1514():
    a=int(input())
    from math import log
    if (int log(a)/log(5))==log(a)/log(5):
        print(0)
    else:
        print("5")
        for i in range(5):
            print(i+a*5-5*(log(a)//log(5)))