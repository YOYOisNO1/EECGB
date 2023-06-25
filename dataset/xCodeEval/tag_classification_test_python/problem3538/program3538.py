def program3538():
    n,t=map(int, input().split())
    s=list(input())
    while(t>0):
        i=0
        while(i<n-1):
            if s[i]=="B" and s[i+1]=="G":
                s[i],s[i+1]=s[i+1],s[i]
                i+=1
            i+=1
        t-=1
    print("".join(s))