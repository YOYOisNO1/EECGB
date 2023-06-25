def program1849():
    input()
    a=input()
    temp =0
    vol=0
    for i in a:
        if ord(i)>=65 and ord(i)<91:
           
            temp=temp+1
    
        if ord(i)==32:
            if temp>vol:
                vol=temp
            temp=0
    if temp>vol:
        vol=temp
    print(vol)