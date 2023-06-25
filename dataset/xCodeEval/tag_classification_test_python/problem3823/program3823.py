def program3823():
    s=input()
    n=len(s)
    res=1
    chars=[];
    for i in range(n):
        c=s[i]
        if (c=='?'):
            if (i==0):
                res=res*9;
            else:
                res=res*10;
        elif (('A'<=c) and (c<='J')):
            if ((c in chars)==False):
                if (i==0):
                    res=res*9
                else:
                    res=res*(10-len(chars));
                chars.append(c);
        if (res==0):
            break;
    print(res)