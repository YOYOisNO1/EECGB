def program427():
    n = int(input())
    d=int(input())
    st=input()
    
    maxindx=0
    till=0
    cnt=0
    for i in range(n):
        maxindx=max(maxindx, i+d)
        if i==till and s[i]==1:
            cnt+=1
            till=maxindx
                    
        if till>=n:
            return cnt