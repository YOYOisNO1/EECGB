def program3907():
    s = list(str(input()))
    lul = 1
    lulu = 1
    a = 1
    l = []
    l1 = []
    for i in range(1,len(s)):
        if int(s[i-1]) > 1:
            c = int(s[i-1]) -1
            w = 9**(len(s) - i)
            lulu = w*c*a
            l1.append(lulu)
        a*=int(s[i-1])
    lulu = 1
    for i in range(len(s)):
        lulu*=(int(s[i]))
    l1.append(lulu)
    lulu = 1
    if s[0] == "1":
        l1.append(9**(len(s) -1))
    print(max(l1))
    
        
        
            
                