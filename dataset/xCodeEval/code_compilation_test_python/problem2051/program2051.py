def program2051():
    arr=[         list(  input()   )      for _ in range (8)      ]
    cw=0
    cb=0
    flag = True
    
    for i,j in range(1,8):
        if ((arr[i][j]) == arr[i-1][j-1]) :
            flag =False
           
    if  (flag == True):
        print("YES")
    else (flag == False):
        print("NO")