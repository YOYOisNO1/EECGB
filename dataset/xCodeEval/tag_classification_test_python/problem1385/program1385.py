def program1385():
    a=["December","January","February","March","April","May","June","July","August","September","October","November"]
    b=input()
    c=int(input())
    print(a[(a.index(b)+c)%12])