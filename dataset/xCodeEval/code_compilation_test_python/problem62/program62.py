def program62():
    import math
    k=int(input())
    ans="codeforces"
    if k==1:
        print (ans)
    else:
        ch=[1]*10
        i=0
        while math.prod(ch)<k:
            c[i]+=1
            i+=1
            if i==10:
                i=0
        for i in range(0, 10):
            print(ans[i]*c[i],end='')