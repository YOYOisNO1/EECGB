def program3039():
    l=[]
    for i in range(2):
        r=list(input()+input())
        while r[0]!="A":r[0],r[1],r[2]=r[2],r[0],r[1]
        r.remove("X");l.append("".join(r))
    print("YES"if l[0]==l[1]else"NO")