def program6218():
    from __future__ import print_function
    r1,c1,r2,c2 = map(int,input().split())
    ans = []
    if((r1==r2 and c1!=c2) or (r1!=r2 and c1==c2)):
        ans.append(1)
    else:
        ans.append(2)
    if((r1+c1)%2 == (r2+c2)%2):
        if((r1+c1)==(r2+c2) or (r1-c1)==(r2-c2)):
            ans.append(1)
        else:
            ans.append(2)
    else:
        ans.append(0)
    ans.append(max(abs(r1-r2),abs(c1-c2)))
    for i in ans:
        print(i,end = " ")