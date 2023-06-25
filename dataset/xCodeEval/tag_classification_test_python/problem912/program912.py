def program912():
    n = int(input())
    s = list(map(int,input().split()))
    c=0
    p=[s[0]]
    for j in range(1,n):
        if(s[j] not in p):
            p.append(s[j])
        else:
            c+=0.00001
            p.append(s[j]+c)
            
    b = sorted(p)
    
    for i in range(n//2):
        print((p.index(b[i])+1),(p.index(b[n-1-i])+1))