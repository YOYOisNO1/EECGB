def program6329():
    from math import *
    inp=int(input())
    li=[]
    while inp>0:
        li.append(inp%10)
        inp//=10
    li.reverse()
    res=len(li)
    for i in range(1,2**len(li)):
        cur=0
        li_num=[]
        for j in range(len(li)):
            if i&(1<<j):
                li_num.append(str(li[j]))
                cur+=1
        num=int(''.join(li_num))
        if sqrt(num)==int(sqrt(num)) and li_num[0]!='0':
            res=min(len(li)-cur,res)
    if res==len(li):
        print("-1")
    else:
        print(res)