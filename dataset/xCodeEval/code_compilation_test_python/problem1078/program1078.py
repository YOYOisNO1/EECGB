def program1078():
    n, a, b = list(int(t) for t in input().rstrip().split(" "))
    
    if a>b:
    	big=a
    	small=b
    else:
    	small=a
    	big=b
    
    pieces=0
    
    while True:
    	pieces+=1
    	pieces_small=small//pieces
    	pieces_big=big//pieces
    	if pieces_small+pieces_big<n and pieces_small!=0 and pieces_big!=0:
    		pieces-=1
    		break
    
    print(pieces)