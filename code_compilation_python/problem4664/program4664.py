    import numpy as np
    
def is_rotate(first_map, second_map):
    	tmp_first_map = first_map[:]
    	for i in range(4):
    		new_matrix = np.rot90(tmp_first_map)
    		if np.array_equal(new_matrix, second_map) or np.array_equal([x[::-1] for x in tmp_first_map], second_map) or np.array_equal([x[::-1] for x in tmp_first_map], second_map):
    			return True
    		tmp_first_map = new_matrix[:]
    	return False
    
    if __name__ == "__main__":
    	n = int(input())
    
    	first_map = []
    	second_map = []
    
    	for i in range(n):
    		first_map.append(list(input()))
    	for i in range(n):
    		second_map.append(list(input()))
    
    	# import code
    	# code.interact(local=locals())
    	if is_rotate(first_map, second_map):
    		print("Yes")
    	else:
    		print("No")