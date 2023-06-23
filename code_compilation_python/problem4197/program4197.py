    s = input()
    n = 0    
    ss = [1, 1, 2, 1, 1, 2, 4, 1, 1, 2, 1, 1, 2, 4, 8]
def render (k):
        global n
        p = []
        while (p.count(0)<k and p.count(1)<k):
            p.append(int(s[n]))
            n+=1
        while (p.count(0)<k): p.append(0)
        while (p.count(1)<k): p.append(1)
        return p
    
def allrender ():
        global n
        global ss
        n = 0
        res = []
    
        for i in ss:
            res.append(render(i))
        return res
    
    rnd = allrender()
    rnd.sort(key = len, reverse = True)
    
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
def razb1(rrazb, st):
        global l
        l0 = []
        l0.append([])
        l0.append([])
        ind = st-1
        for i in rrazb:
            l0[i].append(l[ind])
            ind +=1
        l0[0].extend(l0[1])
        l[st-1:st+len(l0[0])-1] = l0[0]
    
    
    innd = [1, 1, 9, 1, 5, 9, 13, 1, 3, 5, 7, 9, 11, 13, 15]
    for i in range(len(rnd)):
        razb1(rnd[i], innd[i])
    print(16)
    for i in range(len(l)):
        print (l[i], end = " ")
     
     