def program3639():
    l = map(int,input().split())
    s = list(input())
    while l[1]>0:
        i=0
        while i<len(s)-1:
            if s[i]=='B' and s[i+1]=='G':
                s[i],s[i+1]=s[i+1],s[i]
                i=i+2
            else:
                i=i+1
        l[1]=l[1]-1
    print("").join(s)