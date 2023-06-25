def program494():
    s=input()
    s=list(s)
    c=0
    for i in s:
        if(i=='0'):
            c+=1
    if(c>=6 && s[0]=='1'):
        print("yes")
    else:
        print("no")
        
            