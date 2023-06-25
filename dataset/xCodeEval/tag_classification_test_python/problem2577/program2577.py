    a = 1
    b = 0
    
    X = [[0,3],
         [1,2]]
    
def m(a,b):
        r = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    r[i][j]+=a[i][k]*b[k][j]
                    r[i][j]%=1000000007
        return r
    
    power = [X]
    
    for p in range(25): #log_2 of 10^7
        power.append(m(power[-1],power[-1]))
        
    b = map(int, bin(int(input()))[:1:-1])
    r = [[1,0],[0,1]]
    for n,i in enumerate(b):
        if i:
            r = m(r,power[n])
    print(r[0][0])
    