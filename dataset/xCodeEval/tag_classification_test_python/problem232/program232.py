def index(str,char):
        res = []
        for i in range (len(str)):
            if str[i] == char:
                res.append(i)
    
        return res
    
def hasLowerIndex(list1,list2 , char):
        flag = False
        i = 0
        j = 0
        if len(list1)==0 or len(list2) == 0 :
            return False , i ,j
    
        while i < len(list1):
            while j < len(list2):
                if list1[i] < list2[j] :
                    flag = True
                    return flag, list1[i], list2[j]
                else:
                    if char == 'e':
    
                     e.remove(list2[j])
                     j = j-1
                     list2.sort()
    
    
    
    
                    elif char == 'l':
    
                     l.remove(list2[j])
                     j = j-1
                     list2.sort()
                    elif char == 'o':
    
                     o.remove(list2[j])
                     j = j-1
                     list2.sort()
                j=j+1
            i = i+1
    
    
    
    
        return flag , i ,j
    
    h = []
    e = []
    l = []
    o = []
    s = input()
    str = ''
    
    for i in s:
        if i in ['h','e','l','o']:
            str = str + i
    
    h = index(str,'h')
    h.sort()
    e = index(str,'e')
    e.sort()
    l = index(str,'l')
    l.sort()
    o = index(str,'o')
    o.sort()
    ans = 'NO'
    
    
    if  len(h) != 0 and len(e) != 0 and len(l) != 0 and len(o) != 0 :
    
    
        flagHE , heI , heJ  = hasLowerIndex(h,e , 'e')
        flagEL , elI , elJ  = hasLowerIndex(e,l , 'l')
        flagLO , loI , loJ  = hasLowerIndex(l,o , 'o')
    
        flag1 =  False
    
        if flagHE:
            if flagEL :
                if flagLO:
                    for i in l:
                        if elJ < i:
                            flag1 = True
    
                    if flag1:
                        for i in o:
                            if loI < i:
                                ans = 'YES'
    
    
    
    print(ans)