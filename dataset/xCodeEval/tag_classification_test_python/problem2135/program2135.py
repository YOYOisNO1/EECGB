    n, k, d = map(int, input().split())
    
    meme = [[-1 for i in range(2)] for j in range(123)]
    
def fucc(qtd, zeroum):
        global meme
        global n
        global k
        global d
    
        if zeroum == 1 and qtd == n:
            return 1
        
        if qtd >= n:
            return 0
        
        if meme[qtd][zeroum] != -1:
            return meme[qtd][zeroum]
        
        tmp = zeroum
        res = 0
        for i in range(1, k+1):
            if i >= d:
                tmp = 1
            
            res += fucc(qtd+i, tmp)%1000000007
        
        meme[qtd][zeroum] = res
        
        return res 
    
    print(fucc(0,0)%1000000007)
            
    