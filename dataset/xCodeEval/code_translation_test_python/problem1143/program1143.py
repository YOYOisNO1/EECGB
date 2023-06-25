def program1143():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    if(a!=d):
        print("0")
    elif (c>0 and (a==0 or d==0)):
        print("0")
    elif(c>=0 and a==d ):
        print("1")
    else:
        print("0")