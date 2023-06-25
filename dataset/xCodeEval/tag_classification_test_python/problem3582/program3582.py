def program3582():
    n,k=list(map(int,input().split()))
    s=list((" ".join(input())).split())
    a=""
    if n>1:
        for i in range(k):
            b=0
            for g in range(len(s)):
                if s[b]=="B" and s[b+1]=="G":
                    s[b],s[b+1]=s[b+1],s[b]
                    b+=2
                else:
                    b+=1
                if b>=len(s)-1:
                    break
    for i in s:
        a+=i
    print(a)