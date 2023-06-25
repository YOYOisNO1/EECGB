def program579():
    a=input()
    s=b=0
    for i in a:
        if i.isupper():s+=1
        else:b+=1
    if s<=b:print(a.lower())
    else:print(a.upper())
    
        