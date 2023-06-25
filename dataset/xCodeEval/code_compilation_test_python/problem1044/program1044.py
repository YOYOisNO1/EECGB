def program1044():
    k=input()
    m=list(k)
    t=0
    for i in range(len(m)):
        if int(m[i]) in [1,4]:
            continue
        else:
            t=1
            break
    for i in range(len(m)-2):
        if m[i]=="4" and m[i+1]=="4" and m[i+2]=="4":
            t=1
            break
        else if (m[i]=="4" and m[i+1]=="1" and m[i+2]=="4"):
            t=1
            break
        else:
            continue
    if(t==1):
        print("NO")
    else:
        print("YES")