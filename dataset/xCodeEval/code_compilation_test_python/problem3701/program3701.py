    els = ["AC","AG","AL","AM","AR","AS","AT","AU","B","BA","BE","BH","BI","BK","BR","C","CA","CD","CE","CF","CL","CM","CO","CR","CS","CU","DS","DB","DY","ER","ES","EU","F","FE","FM","FR","GA","GD","GE","H","HE","HF","HG","HO","HS","I","IN","IR","K","KR","LA","LI","LR","LU","MD","MG","MN","MO","MT","N","NA","NB","ND","NE","NI","NO","NP","O","OS","P","PA","PB","PD","PM","PO","PR","PT","PU","RA","RB","RE","RF","RG","RH","RN","RU","S","SB","SC","SE","SG","SI","SM","SN","SR","TA","TB","TC","TE","TH","TI","TL","TM","U","V","W","XE","Y","YB","ZN","ZR"]
    s = input()
    
def f(t):
        if t == "":
            return True
        for p in els:
            if t.startswith(p) and f(t[len(p):]):
                return True
        return False
        
    if f(s) || s == "REVOLVER":
        print("YES")
    else:
        print("NO")