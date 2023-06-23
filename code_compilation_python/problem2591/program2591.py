def program2591():
    matrix=[]
    for i in range(4):
        l=list(input())
        matrix.append(l)
    temp=0
    for j in range(3):
        for k in range(3):
            counth=0
            countd=0
            if(matrix[j][k]==#):
                counth+=1
            else:
                countd+=1
            if(matrix[j+1][k+1]==#):
                counth+=1
            else:
                countd+=1
            if(matrix[j+1][k]==#):
                counth+=1
            else:
                countd+=1    
            if(matrix[j][k+1]==#):
                counth+=1
            else:
                countd+=1
            if(counth==4 or countd==4 or counth==3 or countd==3):
                print("YES")
                temp=1
                break
        if(temp==1):
            break
    if(temp==0):
        print("NO")