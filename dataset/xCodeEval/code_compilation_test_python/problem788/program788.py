def program788():
    n,m = map(int,input().split())
    l = []
    for i in range(n):
        l.append(input())
    c = 0
    for i in range(n):
        for j in range(m):
            if l[i][j]=="W":
                if(i>0 and l[i-1][j]=="P"):
                    c=c+1
    		continue
                if(i<n-1 and l[i+1][j]=="P"):
                    c=c+1
        		continue
        	    if(j>0 and l[i][j-1]=="P"):
                    c=c+1
                    continue
        	    if(j<m-1 and l[i][j+1]=="P"):
                    c=c+1
        		continue
    print(c)