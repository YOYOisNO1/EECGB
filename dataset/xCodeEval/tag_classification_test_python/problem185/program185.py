def program185():
    n=int(input())
    l=[0]*12
    for u in range(4):
        s=list(input())
        for i in s:
            if(i.isdigit()):
                l[int(i)]+=1
    for i in l:
        if(i>2*n):
            print("NO")
            break
    else:
        print("YES")