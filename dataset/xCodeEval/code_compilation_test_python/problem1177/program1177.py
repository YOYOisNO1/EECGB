def program1177():
    a,b=map(int,input().split())
    n=list(map(int,input().split()))
    m=list(map(int,input().split()))
    l,y=[],[]
    x,d,w,o= 0,0,0,0
    for z in m :
    	x = x+z
    	l.append(x)
    for i in range(len(l)):
    	q = q+max(0,n[i]-b*l[i])
    n=n[::-1]
    m=m[::-1]
    for p in m :
    	w=w+p
    	d.append(w)
    for r in range(len(y)):
    	o = o+max(0,n[r]-b*y[r])
    if q>o:
    	print("Limak")
    elif q == o:
    	print("Tie")
    else:
    	print("Radewoosh")