def program1584():
    ﻿
    board={}
    for i in range(1,9):
    	row=input()
    	for j in range(1,9):
    		board[i,j]=row[j-1]
    INF=21
    bestw=INF
    bestb=INF
    
    for c in range(1,9):
    	bb=INF
    	bw=INF
    	for r in range(1,9):
    		if(board[r,c]=='B'):
    			bb=min(bb,8-r)
    		elif(board[r,c]=='W'):
    			bb=INF
    	bpresent=False
    	for r in range(1,9):
    		if(board[r,c]=='B'):
    			bpresent=True
    		elif(board[r,c]=='W' and not bpresent):
    			bw=min(bw,r-1)
    	bestw=min(bestw,bw)
    	bestb=min(bestb,bb)
    if(bestw<=bestb):
    	print('A')
    else:
    	print('B')