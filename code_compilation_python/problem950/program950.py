def program950():
    vdef fnc(s):
        str=[]
        for i in s:
            if i=='a' or i=='i' or i=='e' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                pass
            elif ord(i)>=97:
                str.append(chr(46))
                str.append(i)
            else:
                str.append(chr(46))
                str.append(chr(ord(i+22)))
        return str
    t=list(map(int,input().strip().split()))
    s=list(map(int,input().strip().split()))
    for i in fnc(s):
        print(i,end='')