    from sys import stdin
    ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def isValid(ss):
        for i in range(1,len(ss)):
            if ss[i]==ss[i-1]:
                return False
        return True
    ss = input()
    res=0
    if not isValid(ss):
        res=-1
    li = ss[:13]
    li2=ss[13:]
    li_rev=li2[::-1]
    
    ans=''
    
    for x in ch:
        if ss.count(x)>1:
            ans=x
            break
    i_li = ss.index(ans)
    if i_li>12:
        i_rev = i_li;
        i_li=li.index(ans)
        
    else:
        i_rev = li_rev.index(ans)
    
    check = abs(i_li-i_rev)
    if check>1: res=-1
    if res==-1: print('Impossible')
    else:
        print(li+'\n'+li_rev[:i_rev]+li_rev[i_rev+1:])