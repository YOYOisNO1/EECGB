def program5224():
    n=input()
    x=input()
    summ=0
    temp=0
    flag=0
    for i in range(len(x)):
        if(x[i]!='7' and x[i]!='4'):
            flag=1
            break
    if flag==0:
        for i in range(len(x)):
            summ+=int(x[i])
        for i in range(n/2):
            temp+=int(x[i])
        if(temp==summ-temp):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")