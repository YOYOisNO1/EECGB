def program6018():
    a,b=list(map(int,input().split()))
    w,e,l=0,0,0
    for i in range(1,7):
        if abs(a-i)<abs(b-i):
            w+=1
        if abs(a-i)>abs(b-i):
            l+=1
        if abs(a-i)==abs(b-i):
            e+=1
    print(w,e,l)