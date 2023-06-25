def program774():
    import sys
    input = sys.stdin.readline
    I = lambda:list(map(str,input().split()))
     
    n,=I()
    f=0
    count=0
    for i in range(len(n)):
        if n[i] !='1' and n[i]!='4':
            f=f+1
            break
        if n[i]=='4':
            if i==0:
                f=f+1
                break
            count=count+1
        elif n[i]=='1':
            if count>2:
                f=f+1
                break
            count=0
    if count>2:
        f=f+1
    if f==0:
        print("YES")
    else:
        print("NO")