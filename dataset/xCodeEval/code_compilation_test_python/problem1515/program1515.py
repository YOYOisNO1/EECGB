    t = int(input())
    
    answer = []
    
    
    
    # ������� ����� ��������� �������
    
def matrix_count(m):
        
    	x = 0
        
    	for i in m:
            
    		x += sum(i)
        
    	return x
    
    
    
    
    # ���� ����� ��������� �������
    
    for i in range(t):
        
    	matrix = []
        
    	a = input()
        
    	a_list = [int(i) for i in a if i != ' ']
        
    	matrix.append(a_list)
        b = input()
        
    	b_list = [int(i) for i in a if i != ' ']
        
    	matrix.append(b_list)
        y = matrix_count(matrix)
        
    	if y == 4:
            
    		answer.append(2)
        
    	elif y == 3:
            
    		answer.append(1)
        
    	elif y == 2:
            
    		answer.append(1)    
        
    	elif y == 1:
            
    		answer.append(1)
        
    	else:
            
    		answer.append(0)
    
    
    
    
    print(*answer, sep='\n')