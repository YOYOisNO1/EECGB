def program2590():
        l = [""]*4
        a = False
        for i in range(4):
            l[i] = list(input())
         
        for i in range(3):
            if a == False:    
                for j in range(3):
                    if (l[i+1][j+1] == l[i+1][j] and l[i+1][j+1] == l[i][j+1]) or (l[i][j] == l[i+1][j] and l[i][j] == l[i][j+1]) or (l[i][j] == l[i+1][j+1] and l[i][j] == l[i][j+1]) or (l[i][j] == l[i+1][j] and l[i][j] == l[i+1][j+1]):
                        a = True
                        break
           
        if a == True:
            print("YES")
        else:
            print("NO")