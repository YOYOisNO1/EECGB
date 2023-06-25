def program6213():
    qw=input().split(" ")
    r1=int(qw[0])
    c1=int(qw[1])
    r2=int(qw[2])
    c2=int(qw[3])
    opstr=""
    
    mov1=abs(r1-r2)
    mov2=abs(c1-c2)
    
    if mov1==0 or mov2==0:
    	opstr+="1 "
    else:
    	opstr+="2 "
    
    
    if mov1==mov2:
    	opstr+="1 "
    elif mov1%2==mov2%2:
    	opstr+="2 "
    else:
    	opstr+="0 "
    	
    opstr+=str(max(mov1,mov2))
    
    print(opstr)