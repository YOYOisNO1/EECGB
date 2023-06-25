def program3575():
    n,t = map(int,input().split())
    
    s = list(input())
    
    
    for j in range(t):
        troca = []
        for i in range(n-1):
            if s[i] == "B" and s[i+1] == "G":
                troca.append(i)
    
        for i in troca:
            s[i],s[i+1] = s[i+1],s[i]
    
    print("".join(s))