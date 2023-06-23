def program984():
    s=input()
    w=""
    count=0
    for i in range(len(s)):
        if s[i:i+3]=="WUB":
            i=i+3
            w=w+" "
        elif:
            w=w+s[i]
            i=i+1
    print(w)