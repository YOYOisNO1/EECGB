def program69():
    n=int(input("",))
    if(n%7==6):
        mn=((n/7)*2)+1
    else:
        mn=(n/7)*2
    if(n%7==1):
        mx=mn+1
    elif(n%7>=2):
        if(n%7==6):
            mx=mn+1
        else:
            mx=mn+2
    else:
        mx=mn
    print(int(mn,mn))