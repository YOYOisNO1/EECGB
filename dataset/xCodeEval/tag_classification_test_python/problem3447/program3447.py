def program3447():
    n=int(input())
    s=input().strip()
    
    i=0
    c=1
    out=""
    while(i<n):
        out=out+s[i]
        for j in range(c):
            i=i+1
        c=c+1
    print(out)