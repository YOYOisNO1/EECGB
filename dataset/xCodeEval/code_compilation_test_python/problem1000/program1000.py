def program1000():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a==b:
        print(a,end='')
        print(1)
        print(b,end='')
        print(2)
    elif a+1==b:
        print(a,end='')
        print(9)
        print(b,end='')
        print(0)
    elif a==9 && b==1:
        print(9)
        print(10)
    else:
        print(-1)