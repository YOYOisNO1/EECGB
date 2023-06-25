def program120():
    h = []
    v = []
    for i in range(8):
        s = input()
        sl = [i for i in s]
        h.append(sl)
    for i in range(8):
        x = []
        for j in range(8):
            x.append(h[j][i])
        v.append(x)
    ans = 0
    
    for i in h:
        x = list(set(i))
        if(len(x)==1 and x[0]=='B'):
            ans+=1
    for i in v:
        x = list(set(i))
        if(len(x)==1 and x[0]=='B'):
            ans+=1
    if(ans==16):
        print(8)
    else:
        print(ans)