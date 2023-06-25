def program1245():
    n=int(input())
    s=input()
    o=0
    z=0
    for i in range(0,len(s)):
        if s[i]=='0':
            z+=1
        else:
            o+=1
    if z!=o:
        print(1)
        print(s)
    else:
        print(2)
        print(s[0:1],end=' ')
        print(s[1:])