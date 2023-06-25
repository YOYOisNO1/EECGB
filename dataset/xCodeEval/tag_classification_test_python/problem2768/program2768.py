def program2768():
    a=input()
    b=a[::-1]
    li=list(b)
    if a!=b:
        print(len(a))
    elif a==b:
        p=list(a)
        for i in range(len(p)):
            p.pop()
            if p!=p[::-1]:
                print(len(p))
                break
        else:
            print("0")