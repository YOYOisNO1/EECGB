def program1240():
    n=int(input())
    a,b,c=int(input()),int(input()),int(input())
    if(n==1):
        print(0)
    else:
        if(a<b):
            print(a+(n-2)*min(a,c))
        else:
            print(b+(n-2)*min(b,c))