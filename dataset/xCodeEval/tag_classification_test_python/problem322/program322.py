def program322():
    n=int(input())
    s=input()
    c,f=0,0
    for i in s:
        if(i=="x"):
            c+=1
            if(c>2):
                f+=1
        else:
            c=0
    print(f)