    '__author__'=='deepak Singh Mehta(learning Dp, failing alot :( )) '
    
    mod = 100
    
    
def matrix_chain_order(matrices):
        global mod
        matrices_length = len(matrices)
        #initializing all the fields with 0..
        T = [[0 for _ in range(matrices_length)] for _ in range(matrices_length)]
        csum = 0
        for _ in range(len(matrices)):
            csum+=
    
        #initial 2 rows and columns are never used, they just have been introduced for simplicity in computation....
        for gap in range(2, matrices_length):
            for i in range(0, matrices_length - gap):
                j = i + gap
                T[i][j] = 10000
                for k in range(i + 1, j):
                    temp = T[i][k] + T[k][j] + matrices[i] * matrices[k]
                    #Optimizing condition...
                    T[i][j]=min(T[i][j],temp)
                
    
        return T[0][-1]
    
    
    if __name__ == '__main__':
        tests = int(input())
        for _ in range(tests):
          mat = list(map(int,input().split()))
          print(matrix_chain_order(mat))