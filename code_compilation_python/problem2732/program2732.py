def program2732():
    a00=[]
    a01=[]
    a02=[]
    a10=[]
    a11=[]
    a12=[]
    a20=[]
    a21=[]
    a22=[]
    for i in range(3):
        q=input().split()
        a00.append(q[0])
        a01.append(q[1])
        a02.append(q[2])
    input()
    for i in range(3):
        q=input().split()
        a10.append(q[0])
        a11.append(q[1])
        a12.append(q[2])
    input()
    for i in range(3):
        q=input().split()
        a20.append(q[0])
        a21.append(q[1])
        a22.append(q[2])
    x,y=map(int,input().split())
    x,y=(x-1)%3,(y-1)%3
    if x==0 and y==0:
        for i in a00:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a00[i][j]=='.':
                            a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==0 and y==1:
        for i in a01:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a01[i][j]=='.':
                            a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==0 and y==2:
        for i in a02:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a02[i][j]=='.':
                            a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==1 and y==0:
        for i in a10:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a10[i][j]=='.':
                            a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==1 and y==1:
        for i in a11:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a11[i][j]=='.':
                            a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==0 and y==2:
        for i in a02:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a02[i][j]=='.':
                            a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==2 and y==0:
        for i in a20:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a20[i][j]=='.':
                            a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==2 and y==1:
        for i in a21:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a21[i][j]=='.':
                            a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    if x==2 and y==2:
        for i in a22:
            if '.' in i:
                for i in range(3):
                    for j in range(3):
                        if a22[i][j]=='.':
                            a22[i]=a22[i][:j]+'!'+a2[i][j+1:]
                break
        else:
            for i in range(3):
                for j in range(3):
                    if a00[i][j]=='.':
                        a00[i]=a00[i][:j]+'!'+a00[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a01[i][j]=='.':
                        a01[i]=a01[i][:j]+'!'+a01[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a02[i][j]=='.':
                        a02[i]=a02[i][:j]+'!'+a02[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a10[i][j]=='.':
                        a10[i]=a10[i][:j]+'!'+a10[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a11[i][j]=='.':
                        a11[i]=a11[i][:j]+'!'+a11[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a12[i][j]=='.':
                        a12[i]=a12[i][:j]+'!'+a12[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a20[i][j]=='.':
                        a20[i]=a20[i][:j]+'!'+a20[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a21[i][j]=='.':
                        a21[i]=a21[i][:j]+'!'+a21[i][j+1:]
            for i in range(3):
                for j in range(3):
                    if a22[i][j]=='.':
                        a22[i]=a22[i][:j]+'!'+a22[i][j+1:]
    for i in range(3):
        print(a00[i],a01[i],a02[i])
    print()
    for i in range(3):
        print(a10[i],a11[i],a12[i])
    print()
    for i in range(3):
        print(a20[i],a21[i],a22[i])