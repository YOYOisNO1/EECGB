def program1285():
    rc=input().split(' ')
    row=int(rc[0])
    col=int(rc[1])
    
    
    picture=[]
    for x in range(0,row):
    	picture.append(input().split(' ')
    
    c=0
    for i in range(0,row):
    	for j in range(0,col):
    		if picture[i][j]=="C" or picture[i][j]=="M" or picture[i][j]=="Y":
    			c=c+1
    
    if c==0:
    	print"#Black&White"
    else:
    	print "#Color"