def program3637():
    
    t = map(int,input().split())
    
    f=""
    s = input()
    st = list(s)
    i = 0 
    time = t[1]
    for t in range(time):
        while i < len(s) - 1:
            if st[i] == "B" and st[i+1] == "G":
                st[i],st[i+1] = "G","B"
                #f = f + "GB"
                i += 2
            else:
                #f = f + st[i]
                i += 1
        i = 0     
    for l in st:
        f = f + l
    print(f)    