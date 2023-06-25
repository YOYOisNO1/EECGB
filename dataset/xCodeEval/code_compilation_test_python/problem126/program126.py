def solution(N, t, P):
    
        cache = [[0 for j in range(N+1)] for i in range(t+1)]
    
        cache[0][0] = 1
    
        for i in range(t):
    
            for j in range(N+1):
    
                if j == N:
    
                    cache[i+1][j] += cache[i][j]
    
                else:
    
    
    
                    cache[i+1][j+1] += cache[i][j] * P
    
                    cache[i+1][j] += cache[i][j] * (1 - P)
    
        answer = 0 
    
        for j in range(N+1):
    
            answer += cache[t][j] * j
    
        return round(answer,6)