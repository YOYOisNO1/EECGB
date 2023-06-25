def program3591():
    nk=input().split()
    n=int(nk[0])
    k=int(nk[1])
    s=list(input())
    for k_qtr in range (k) :
    
        i=1
        while(i<n):
            b=0
            if s[i-1]=="B" and s[i]=="G":
                s[i-1],s[i]="G","B"
                b=b+1
            if (b==1):
                i=i+1
            i=i+1
    print("".join(map(str,s)))