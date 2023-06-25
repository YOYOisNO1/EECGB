def program1937():
    a, b=map(int, input(). split())
    if b==a:
        print(int(str(a)+"2"), int(str(b)+"3"))
    elif a==9 and b==1:
        print(99, 100)
    elif b-a>0 and b-a<2:
        print(int(str(a)+"9"), int(str(b)+"0"))
    else:
        print(-1)
    