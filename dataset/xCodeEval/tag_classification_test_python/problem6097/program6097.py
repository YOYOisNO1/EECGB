def cntof(p,c):
        cnt=0
        for i in range(len(p)-len(c)+1):
            if p[i:i+len(c)]==c:
                cnt+=1
        # print(p,c,cnt)
        return cnt
    s=input()
    l=len(s)
    maxl=0
    for i in range(1,l):
        for j in range(l-i+1):
            if cntof(s,s[j:i+j])>1:
                if i>maxl:maxl=i
    print(maxl#,cntof("ababa","abab"))