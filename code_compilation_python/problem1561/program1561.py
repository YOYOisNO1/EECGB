def program1561():
    import sys
    
    Lines = []
    for Line in sys.stdin:
      Lines.append(Line.rstrip('\n'))
    
    
    
    # lines=["7 11",
    # "4 7",
    # "6 4",
    # "5 1",
    # "1 4",
    # "5 4",
    # "1 2",
    # "3 4",
    # "4 2",
    # "6 1",
    # "3 1",
    # "7 1"]
    
    
    n,m = list(map(int,lines[0].split()))
    del(lines[0])
    
    #G=[[] for _ in range(n)]
    G=[[0 for i in range(n)] for j in range(n)]
    for i in range(m):
       a,b=list(map(int,lines[i].split()))
       a = a-1
       b = b-1
       G[a][b]=1
       G[b][a]=1
    
    if (n<=6):
    	print(m)
    	exit(0)
    else:
        ctr = 2e9;
        for i in range(n):
            for k in range(n):
                temp = 0
                for j in range(n):            
                    if(G[i][j]==1 and G[k][j]==1):
                    	temp+=1
                ctr = min(ctr, temp)
        print(m-ctr)
    