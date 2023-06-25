    #!/usr/bin/env python
    
    import copy
    
def read():
        ret = []
        for i in range(3):
            ret.append(map(int, input().split()))
        n = int(input())
        return ret, n
    
    
def work((mat, n)):
        curMin = copy.deepcopy(mat)
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    curMin[i][j] = min(curMin[i][j], curMin[i][k] + curMin[k][j])
        
        for loop in range(n - 1):
            nexMin = [[-1 for j in range(3)] for i in range(3)]
            for s in range(3):
                for t in range(3):
                    m = -1
                    for i in range(3):
                        if i != s and i != t:
                            m = i
                    
                    A = 0
                    A += min(curMin[s][m], curMin[s][t] + curMin[t][m])
                    A += mat[s][t]
                    A += min(curMin[m][t], curMin[m][s] + curMin[s][t])
                    
                    B = 0
                    B += min(curMin[s][t], curMin[s][m] + curMin[m][t])
                    B += mat[s][m]
                    B += min(curMin[t][s], curMin[t][m] + curMin[m][s])
                    B += mat[m][t]
                    B += min(curMin[s][t], curMin[s][m] + curMin[m][t])
    
                    nexMin[s][t] = min(A, B)
    
            curMin = nexMin
    
        print(curMin[0][2])
    
    
    if __name__ == "__main__":
        work(read())