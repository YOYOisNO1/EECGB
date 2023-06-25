def program1486():
    a=input()
    b=input()
    c=str(int(a)+int(b))
    aa,bb,cc='','',''
    for i in a: if i!='0': aa+=i
    for i in b: if i!='0': bb+=i
    for i in c: if i!='0': cc+=i
    if int(aa)+int(bb)==int(cc): print("YES") else: print("NO")