def program2608():
    line = input().split()
    
    for i in range(len(line)):
    	line[i] = int(line[i])
    
    if(line[0] - line[1] < line[2]+1):
    	print(line[0] - line[1])
    else:
    	print(line[2]+1)