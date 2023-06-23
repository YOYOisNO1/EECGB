def check(i,j,matrix) :
        c = []
        if i+4<10 :
            s= ""
            s = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j] + matrix[i+4][j]
            c.append(s)
            if j+4<10 :
                t = ""
                t = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3] + matrix[i+4][j+4]
                c.append(t)
        if j+4<10 :
            s = ""
            s = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3] + matrix[i][j+4]
            c.append(s)
        for i in range(len(c)):
            if c[i]=='XX.XX' or c[i]=='.XXXX' or c[i]=='X.XXX' or c[i] == 'XXX.X' or c[i]=='XXXX.':
                return True
                break
        else :
            return False
    
    matrix = []
    for i in range(10):
        s = input()
        matrix.append(s)
    flag = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j]=='X' or matrix[i][j]=='.' :
                if check(i,j,matrix) :
                    print("YES")
                    flag = 1
                    break
        if flag == 1 :
            break
    else :
        print("NO")