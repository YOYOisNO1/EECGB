def program3553():
    n,et=list(map(int,input().split()))
    st=input()
    s=list(st)
    t=0
    i=1
    while(et>0):
        i=1
        while i<n:
            if(s[i-1]=='B' and s[i]=='G'):
                temp=s[i-1]
                s[i-1]=s[i]
                s[i]=temp
                i=i+2
            else:    
                i=i+1    
        et=et-1    
    for i in range(0,len(s)):
        print(s[i],end="")
            