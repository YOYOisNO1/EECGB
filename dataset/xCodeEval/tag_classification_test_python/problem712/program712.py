def program712():
    s=input()
    if len(s)==1:
        print(s)
    else:
        l=[]
        for i in range(0,len(s),2):
            l.append(s[i])
        l.sort()
        for i in range(0,len(l)-1):
            print(l[i],"+",end="",sep="")
        print(l[i+1])