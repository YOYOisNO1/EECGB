def program403():
    a=input()
    b=input()
    c=input()
    
    x=[0,0,0]
    ans=""
    for i in range(3):
        if a[1]=="<":
            x[ord(a[2])-65]+=1
            x[ord[a[0])-65]-=1
        else:
            x[ord(a[0])-65]+=1
            x[ord[a[2])-65]-=1
    y=[]
    for i in x:
        y.append(i)
    y.sort()
    if y!=[-2,0,2]:
        print("Ïmpossible")
    else:
        for i in range(3):
            if x[i]==2:
                ans+=chr(i+65)
        for i in range(3):
            if x[i]==0:
                ans+=chr(i+65)
        for i in range(3):
            if x[i]==-2:
                ans+=chr(i+65)