def program1107():
    v,a,b=list(map(int,input().split()))
    c=0
    m=True
    if a%2==0:
        v-=a-2
        m=False
    else:
        v-=a-1
        m=False
    if v-b>=2:
        m=False
        if b%2==0:
            v-=v-(b+1)
        else:
            v-=v-(b+2)
    if m==True:
        print("Final!")
    for i in range(8):
        v/=2
        if v<=2:
            c+=1
            break
       else:
            c+=1
    print(c)