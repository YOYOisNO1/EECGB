def program3417():
    # import sys
    # sys.stdin=open("input.in",'r')
    # sys.stdout=open("out1.out",'w')
    r,g,b=map(int,input().split())
    t=29
    while r+b+g:
    	if r>2 :
    		t+=1
    		r-=2
    	else:
    		t+=1
    		r=0
    	if r+b+g==0:
    		break	
    	if g>2:
    		t+=1
    		g-=2
    	else:
    		t+=1
    		g=0
    	if r+b+g==0:
    		break
    	if b>2:
    		t+=1
    		b-=2
    	else:
    		t+=1
    		b=0	
    print(t)		