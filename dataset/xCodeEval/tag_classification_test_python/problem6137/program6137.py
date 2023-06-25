def program6137():
    m=map(int,input().split())
    r1=m[0]
    c1=m[1]
    r2=m[2]
    c2=m[3]
    #for rooks
    rook=2
    if r1==r2 or c1==c2:
    	rook-=1
    king=max(abs(r2-r1),abs(c1-c2))
    bishop=0
    if (r1+c1)%2==(r2+c2)%2:
    	if r2+c2==r1+c1 or (r1+9-c1)==(r2+9-c2):
    		bishop=1
    	else:
    		bishop=2
    ans=str(rook)+" "+str(bishop)+" "+str(king)
    print(ans)
    