    n = int(input())
    a = input()
    b = ""
    for i in range(len(a)):
        if a[i] == "(":
            b = b + "_"
            b = b + "("
        elif a[i] == ")":
            b = b + ")"
            b = b + "_"
        else:
            b = b + a[i]
    a = b
    
def skob(a):
        ind = 0
        l = []
        for i in range(len(a)):
            if a[i] == "(" and ind == 0:
                ind = i
            elif a[i] == ")":
                l = l + [a[ind:i]]
                ind = 0
                
        return l
    
def vires(a):
        a = a + "("
        ind = 0
        b = ""
        for i in range(len(a)):
            if a[i] == "(":
                b = b + a[ind:i]
            elif a[i] == ")":
                ind = i + 1
        return b
    
def slovo(a):
        a = a + "_"
        ind = 0
        pl = []
        l = []
        for i in range(len(a)):
            if a[i] == "_":
                pl = pl + [a[ind:i]]
                ind = i + 1
                
        for i in range(len(pl)):
            if pl[i] != "" and pl[i] != "_" and pl[i] != "(" and pl != ")":
                l = l + [pl[i]]
                
        return l
    
def slovinskob(l):
        pl = []
        a = ""
        fl = False
        for i in range(len(l)):
            if fl == True:
                a = a + "_"
            for j in range(len(l[i])):
                a = a + str(l[i][j])
            fl = True
        return a
    
def maxsumm(l):
        s = 0
        maxsumm = 0
        ind = 0
        for i in range(len(l)):
            s = len(l[i])
            if s > maxsumm:
                maxsumm = s
        
        return maxsumm
    
def vivod(a):
        l2 = skob(a)
        a = vires(a)
        l1 = slovo(a)
        a = slovinskob(l2)
        l2 = slovo(a)
        s = maxsumm(l1)
        return s, len(l2)
    
    c,b = vivod(a)
    print(c,b)