def program3129():
    n,m=[int(i) for i in input().split()]#c=()
    c=m//9
    d=m%9
    k=n*[0]
    if m<=9 and n==1:
        print(m,m)
    if m<=9 and n>1:
        if m==1:
            k[0]=1
            k=list(map(str,k))
            print("".join(k),"".join(k))
        else:
            if m==0:
                print(-1,-1)###
            else:
                u=k
                u[0]=1
                u[n-1]=m-1
               # print(u)
                u=list(map(str,u))
                uu="".join(u)
                s=n*[0]
     #           s=k
                s[0]=m
                s=list(map(str,s))
                #print(s)
                ss="".join(s)
                print(uu,ss)
    if c>=n:
        if c>n:
            print(-1,-1)
        if c==n and d!=0:
            print(-1,-1)
        if c==n and d==0 and n!=1:##1!
            t=n*["9"]###list
            t="".join(t)
            print(t,t)       
    else:
        if m>9:
    #    k.append(d)
            for i in range(c):# add 9#change
     #       k.append(9)
                k[i]=9
            if d!=0:
                k[c]=d
            k=list(map(str,k))
            zz="".join(k)
            if c+1==n:
                k.reverse()
                k=list(map(str,k))
                mm="".join(k)
                print(mm,zz)
            else:#d=0 qingkuang
                if d!=0:
                    k[c]=d-1
                else:
                    k[c]=0
                    k[c-1]=8###
                k[n-1]=1
                k.reverse()
                k=list(map(str,k))
                mm="".join(k)
                print(mm,zz)#kk