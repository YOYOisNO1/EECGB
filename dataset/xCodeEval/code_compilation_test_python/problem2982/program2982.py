def program2982():
    n=int(input())
    a=list(map(int,input().split()))
    month1=[31,28,31,30,31,30,31,31,30,31,30,31]
    month2=[31,29,31,30,31,30,31,31,30,31,30,31]
    if a.count(29)>1 :
        print('NO')
    elif a.count(28)==1 and a.count(29)==1 :
        a[a.index(29)]=28
    elif a.count(29)==1 :
        a[a.index(29)]=28
    solved=0
    first=[]
    i=0
    b=[]
    for i in range(len(month1)):
        b.append(month1[i])
    for i in range(b.count(a[0])):
        first.append(b.index(a[0]))
        b[b.index(a[0])]=-1
    
    
    
    counter=month1.index(a[0])
    cycle=0
    for u in range(month1.count(a[0])):
        i=0
        counter=first[u]
        while 1 :
            if counter>=12 :
                counter-=12
            if a[i]==month1[counter]:
                counter+=1
                i+=1
            else :
                cycle+=1
                break
            if i==n :
                print('YES')
                solved=1
                break
            if solved==1 :
                break
    if solved==0 :
        print('NO')