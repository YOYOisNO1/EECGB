def program6134():
    bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
    #start = time.clock()
    r1,c1,r2,c2=map(int,input().split())
    ans=[]
    chk=0
    if r1==r2 and c1==c2:
        print(0,0,0)
        exit()
    if r1==r2 or c1==c2:
        ans.append(1)
    else:
        ans.append(2)
    
    if (r1+c1)%2!=(r2+c2)%2:
        ans.append(0)
    else:
        for i in range(4):
            a,b=r1,c1
            while 1:
                a+=bs[i][0]
                b+=bs[i][1]
                if a==r2 and b==c2:
                    chk=1
                    break
                if a<0 or a>8 or b<0 or b>8:
                    break
            if chk==1:
                ans.append(1)
                break
            elif i==3:
                ans.append(2)
    ans.append(max(abs(r2-r1),abs(c2-c1)))
    print(' ').join(map(str,ans))