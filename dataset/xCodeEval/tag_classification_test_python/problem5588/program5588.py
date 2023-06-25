    mat1=[input() for l in range(10)]
    mat2=list(reversed(mat1))
    mat3=[]
    
    for l in mat1:
        mat3.append(l[::-1])
    
def horizontal(inp,i,j):
        s=''
        for k in range(j, j+5):
            s=s+inp[i][k]
        return s
    
def vertical(inp,i, j):
        s=''
        for k in range(i, i+5):
            s=s+inp[k][j]
    
        return s
    
def diagonal(inp,i,j):
        first=range(i,i+5,1)
        second=range(j,j+5,1)
        s=''
        for k, l in zip(first, second):
            s+=inp[k][l]
    
        return s
    
def checker(s):
        if '0' in s:
            return False
    
        else:
            if s.count('X')<4:
                return False
    
            else:
                if '.' not in s:
                    return False
    
        return True
    
    
def solve(mat):
        for i in range(6):
            for j in range(6):
                if (checker(horizontal(mat,i, j))):
                    return True
                if (checker(vertical(mat,i,j))):
                    return True
    
                if checker(diagonal(mat,i,j)):
                    return True
    
        return False
    
    
    a=solve(mat1)
    b=solve(mat2)
    c=solve(mat3)
    
    if a or b or c:
        print("YES")
    else:
        print("NO")