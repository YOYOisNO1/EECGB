def program2492():
    a=[]
    for i in range(3):
        x=input();a.append(x)
    ans="YES"
    for i in range(3):
        for j in range(3):
            if a[i][j]=='X' and a[2-i][2-j]<>'X':   ans="NO"
    print(ans)