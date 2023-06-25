def program2390():
    l=input().strip()
    occur=0
    chance=1
    l="K"+l+"V"
    for i in range(1,len(l)-2):
        if l[i:i+2]=="VK":
            occur+=1
        elif (l[i:i+2]=="VV" and l[i+2]!="K" and chance!=0):
            occur+=1
            chance-=1
        elif (l[i:i+2]=="KK" and l[i-1]!="V" and chance!=0):
            occur+=1
            chance-=1
    print(occur)