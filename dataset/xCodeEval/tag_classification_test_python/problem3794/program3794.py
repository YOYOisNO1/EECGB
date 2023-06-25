def program3794():
    a=int(input())
    if (a>0):
            print(a)
    else:
        s=str(a)
        s1=s[:-1]
        s2=s[:-2]+s[-1:]
        ss1=int(s1)
        ss2=int(s2)
        print(max(ss1,ss2))