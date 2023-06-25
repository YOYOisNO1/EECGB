def program6074():
    P=[]
    ans=""
    for _ in range(8):
    	x,y=list(map(int,input().split()))
    	P.append((x,y))
    
    X,Y=map(list, zip(*P))
    X.sort()
    Y.sort()
    y=Y[3]
    x=X[3]
    if(len(set(X))==3 and len(set(Y))==3 and (x,y) not in P and len(set(P))==len(P)):
    	ans="respectable"
    else:
    	ans="ugly"
    
    print(ans)