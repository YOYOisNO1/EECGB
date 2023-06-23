def program3951():
    t=input()
    n=input()
    a=[]
    for x in range(0,9):
        if x!=5 and str(x) in t:
            if x==2:
                a.append((n.count("2")+n.count("5"))/(t.count("2")+t.count("5")))
            elif x==6:
                a.append((n.count("6")+n.count("9"))/(t.count("6")+t.count("9")))
            else:
                a.append(n.count(str(x))/t.count(str(x)))
            
    print sorted(a)[0]