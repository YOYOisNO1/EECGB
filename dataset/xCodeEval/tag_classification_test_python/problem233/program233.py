def program233():
    d=list(input(""))
    k=["h","e","l","l","o"]
    l=0
    for i in d:
        if  l<5:
            if i == k[l]:
                l+=1
        else:
            pass
    if l==5:
        print("YES")
    else:
        print("NO")