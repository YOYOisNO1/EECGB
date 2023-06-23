def program1142():
    a=[]
    for i in range(3):
        a.append(int(input()))
    b=min(a)
    c=max(a)
    a.remove(b)
    d=min(a)
    print(max((b*d)*c,(b+d)*c),(b+c+d),(b*c*d)))