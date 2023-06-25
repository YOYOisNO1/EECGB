def program1991():
    n=int(input())
    l=list(map(int,input().split()))
    s=list(set(l))
    if len(s)<3:
        print("NO")
    else:
        s.sort()
        for i in range(len(s)-2):
            if (s[i+2]-s[i+1]=1) and (s[i+1]-s[i]==1):
                print("YES")
                break
        else:
            print("NO")