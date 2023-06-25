def program6063():
    import sys
    n=int(input())
    list1=[[0 for i in range(6)]for i in range(6)]
    for i in range(n):
        a,b=map(int,input().split())
        list1[a][b]=1
        list1[b][a]=1
        
    for i in range(1,6):
        for j in range(1,6):
            for k in range(1,6):
                if(i!=j and j!=k and i!=k):
                    if(list1[i][j]==1 and list1[j][k]==1 and list1[k][i]==1):
                        # print(i,j,k)
                        f=1
                        print("WIN")
                        sys.exit()
                    elif(list1[i][j]==0 and list1[j][k]==0 and list1[k][i]==0):
                        # print(i,j,k)
                        print("WIN")
                        sys.exit()
                        
                        
    print("FAIL")