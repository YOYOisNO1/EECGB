def program1683():
        import sys
    n = int(input())
    lst = list(input())
    s=0
    z=0
    #print(len(lst))
    lst1 = ["C", "Y", "M"]
    n=0
    for i in range(len(lst)-1):
        if lst[i]=="?":
            n+=1
    for i in range(len(lst)-1):
        if lst[i]=='?':
            s+=1
            if i==0:
                s+=1
            elif i==len(lst)-1:
                s+=1
            elif i>0 and i<len(lst)-1:
                if lst[i-1]==lst[i+1]:
                    s+=1
                else:
                    z+=2
                    s+=1
        if lst[i]==lst[i+1]:
            z=1
    #print(z,s)
    if s!=0:
        if z%s==0 and z!=0:
            print('No')
            sys.exit()
        elif z%s==1:
            print('No')
            sys.exit()
    if n==len(lst)-1:
        print("Yes")
    elif z==1:
        print("No")
    elif s==0:
        print("Yes")
    else:
        print("Yes")