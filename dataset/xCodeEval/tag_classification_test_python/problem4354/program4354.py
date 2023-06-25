def program4354():
    a=input()
    for i in range(1):
        if len(a)%2==0:
            print(a[(len(a)//2)-1],end="")
            b=a[:(len(a)//2)-1]
            b=b[::-1]
            c=a[(len(a)//2):]
            for j in range(len(b)):
                print(c[j]+b[j],end="")
            print(c[len(b)])
        else:
            print(a[len(a)//2],end="")
            b=a[:(len(a)//2)]
            b=b[::-1]
            c=a[(len(a)//2)+1:]
            for j in range(len(b)):
                print(c[j]+b[j],end="")
            print()
                        
                        