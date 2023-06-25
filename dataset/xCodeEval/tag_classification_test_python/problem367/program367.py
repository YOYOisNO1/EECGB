def iqTest(test):
        for i in range(3):
            for j in range(3):
                white=0
                black=0
                for kletka in [test[i][j],test[i][j+1],\
                test[i+1][j],test[i+1][j+1]]:
                    if kletka=='.':
                        white+=1
                    else:
                        black+=1
                if white==3 or black==3 or white==4 or black==4:
                    return 'YES'
        return 'NO'
    
    test=[]
    
    for i in range(4):
        test.append(input())
    
    print(iqTest(test))