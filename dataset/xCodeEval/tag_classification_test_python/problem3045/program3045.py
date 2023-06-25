def program3045():
    r=0;
    n=input()
    s=input()
    j=0
    for i in range(1,len(s)):
        if s[i]==s[j]: r+=1;
        else: j=i
    print(r)