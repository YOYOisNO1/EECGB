def program1848():
    n=input()
    a=input().split()
    t=[]
    for i in a:
        p=0
        for j in i:
            if j.isupper():
                p +=1
        t +=[p]
    print(max(t))