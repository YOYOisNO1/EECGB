def program3305():
    x=int(input())
    b=False
    for i in range(1,200):
        if i*(i+1) / 2 == x:
           b=True
           break
    if b:
        print("YES")
    else:
        print("NO")    