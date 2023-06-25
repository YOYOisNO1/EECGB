    n = int(input())
    S = list(input())
    
def count_all(s):
        cnt=0
        l_cnt=1
        for c in s[1:]:
            if c==')':
                l_cnt-=1
            else:
                l_cnt+=1
            if l_cnt==0:
                cnt+=1
        return cnt
    if S!=list('()'*(n//2)) and S!=list(')'+'()'*(n//2-1)+'('):
        print(n // 2)
        print(1, 1)
    else:
        res=0
        l,r =1,1
        lc=rc=0
        
        for c in S:
            if c=="(":
                lc+=1
            else:
                rc+=1
        
        if lc==rc:
            for i in range(n):
                for j in range(i,n):
                    ss=S[:]
                    if ss[i]==ss[j]:
                        continue
                    ss[i],ss[j]=ss[j],ss[i]
                    t=0
                    t_min=n
                    m=0
                    for k in range(n):
                        if ss[k]==")":
                            t-=1
                        else:
                            t+=1
                        if t<t_min:
                            t_min,m=t,k
                    sss=ss[m+1:]+ss[:m+1]
                    temp = count_all(sss)
                    if temp>=res:
                        # print(sss)
                        res=temp
                        l,r=i+1,j+1
        print(res)
        print(l,r)