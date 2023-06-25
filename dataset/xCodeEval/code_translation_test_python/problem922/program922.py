def program922():
    a=input()
    b=input()
    c=input()
    dic={a:"F",b:"M",c:"S"}
    if(a==b and a!=c):
        if(a=="paper"and c=="scissors"):
            print(dic[c])
        elif(c=="paper" and a=="rock"):
            print(dic[c])
        elif(a=="scissors" and c=="rock"):
            print(dic[c])
        else:
            print("?")
    elif(b==c and a!=c):
        if(b=="paper"and a=="scissors"):
            print(dic[a])
        elif(a=="paper" and b=="rock"):
            print(dic[a])
        elif(c=="scissors" and a=="rock"):
            print(dic[a])
        else:
            print("?")
    elif(a==c and b!=c):
        if(a=="paper"and b=="scissors"):
            print(dic[b])
        elif(b=="paper" and c=="rock"):
            print(dic[b])
        elif(a=="scissors" and b=="rock"):
            print(dic[b])
        else:
            print("?")
    else:
        print("?")
    