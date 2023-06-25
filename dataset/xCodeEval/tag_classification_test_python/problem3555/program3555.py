def program3555():
    a,b=map(int,input().split())
    s=list(str(input()))
    for i in range(b):
        m=0
        while m<a-1:
            if s[m]=="B" and s[m+1]=="G":
                s[m],s[m+1]=s[m+1],s[m]
                m+=1
            m+=1
    k=""
    for i in s:
        k+=str(i)
    print(k)