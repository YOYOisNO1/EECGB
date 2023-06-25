    n=int(input())
    p=[]
    answer=[]
    
    for j in range(n):
        p.append(list(map(int, input().split())))
    
def g(i):
        for j in range(n):
            for k in range(j+1, n):
                if i==j or i==k:
                    continue;
                if sum((p[j][l] - p[i][l]) * (p[k][l] - p[i][l]) for l in range(5)) > 0:
                    return ;
        answer.append(i+1)
        
    for i in range(n):
        g(i)
    
    print(len(answer))
    print(*answer)