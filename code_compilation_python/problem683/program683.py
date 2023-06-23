def program683():
    n=int(input())
    s=input().strip()
    flag=1 
    if n==1:
        if s=="0":
            print("Yes")
        else:
            print("No")
    elif n==2:
        if s!="00":
            print("Yes")
        else:
            print("No")
    else n>=3:
        if s[:2]=="00":
            flag=0
        for i in range(1,n-1):
            t=s[i-1]+"1"+s[i+1]
            if int(t[0])^int(t[1])==1 or int(t[1])^int(t[1])==1:
                flag=0 
                break
        if s[n-2:n]=="00":
            flag=0
        for i in range(n-1):
            if s[i:i+2]=="11":
                flag=0
                break
        if flag==1:
            print("Yes")
        else:
            print("No")