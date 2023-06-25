def program2675():
    L=input()
    a=0
    b=0
    for c in L:
        if c=='o':
            a+=1
        else :
            b+=1
    if (a==0)||(b%a==0) :
        print("YES")
    else:
        print("NO")