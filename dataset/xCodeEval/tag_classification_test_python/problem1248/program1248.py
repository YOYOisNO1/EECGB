def program1248():
    a=int(input())
    b=input()
    s=0
    k=0
    for i in range(a):
        if b[i]=='-' and k>0:
            if s>0:
                s-=1
        elif b[i]=='+':
            k+=1
            s+=1
    print(s)