def program6099():
    s=input()
    ls=len(s)
    j=2
    for i in range(ls-1,0,-1):
        q=[]
        for k in range(j):
            w=s[k:k+i]
            if w in q:
                print(i)
                exit()
            else:
                q.append(w)
        j+=1
    print(0)