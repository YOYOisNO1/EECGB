def program621():
    a=input()
    b=["a","e","i","o","u"]
    temp=True
    for i in range(len(a)):
        if a[i] not in b and a[i]!="n":
            if i!=len(a)-1:
                if a[i+1] in b:
                    continue
                else:
                    temp=False
                    print("NO")
                    break
            else:
                temp=False
                pprint("NO")
            else:
                continue
            
    if temp==True:
        print("YES")
    
        