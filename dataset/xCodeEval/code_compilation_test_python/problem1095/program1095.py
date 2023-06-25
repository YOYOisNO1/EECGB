def program1095():
    a,b=list(map(int,input()s.plit()))
    
    c=a
    while a<b:
        a=a//b
        r=a%b
        c+=r
    print(c)    