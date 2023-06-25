def program1496():
    n=int(input())
    r=n%4
    if(r==2):
        r=1
    else:
        if(r==3):
            r=0
    print(r)