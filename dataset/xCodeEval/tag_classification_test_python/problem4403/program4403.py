def program4403():
    s=input()
    s1=s[0]
    sm=s[len(s)-1]
    s=s1+s[1:len(s)-1].replace('dot','.')+sm
    for i in range(1,len(s)-1):
        if s[i]=='a' and s[i+1]=='t':
            s=s[:i]+'@'+s[i+2:]
            break
    print(s)