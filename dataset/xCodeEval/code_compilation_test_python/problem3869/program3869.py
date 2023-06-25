def program3869():
    a=input()
    g,p={},{'R':0,'B':0,'Y':0,'G':0}
    for i in range(len(a)):
        if a[i] in 'BYRG':
            g[i%4]=a[i]
    for i in range(len(a)):
        if a[i]=="!": p[g[i%4]]+=1
    print(p['R'],p['B],p['Y'],p['G'])