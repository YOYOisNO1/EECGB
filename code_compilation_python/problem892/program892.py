def program892():
    n=int(input())
    s=input()
    F=[[None]*n for i in range(n)]
    # x=set()
    # for i in s:
    #     x.add(i)
        
    
    for i in range(n):
        F[i][i]=1
    
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            temp=[]
            t=i
            f=0
            for k in range(i+1,j+1):
                if s[k]==s[i]:
                    temp.append(k)
            for q in temp:
                if q-t>=2:
                    f+=F[t+1][q-1]
                t=q
            if t<j:
                f+=F[t+1][j]
            
            
            F[i][j]=min(f,F[i+1][j])+1
        
    print(F[0][n-1])                       
    # s=input()
    # a=[]
    # for i in range(1,len(s)):
    #    if s[i]==s[0]:
    #     a.append(i)
    # t=0
    # for i in a:
    #     if i-t>=2:
    #         print(str(t)+' '+str(i))
    #     t=i         
    
                             