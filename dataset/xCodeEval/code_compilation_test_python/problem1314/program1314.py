def program1314():
    a=int(input())
    b=str(input())
    c=''
    k=0
    z=b[:1]
    b+="W"
    z=0
    for i in b:
         if i=="B" :
            k+=1
        elif i!="B" and k!=0:
            c+=str(k)+" "
            z+=1
            k=0
    print(z)
    print(c[:-1])