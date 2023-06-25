    # 887B
    cubes_sets = []
    
def myor(smlist):
            buff_list = [1, 1, 1]
            for x in smlist:
                    for y in range(3):
                            buff_list[y] = min(x[y], buff_list[y])
            return buff_list
    
def can_make(num):
            buff_num = str(num)
            if len(buff_num) == 1:
                    if buff_num in cubes_sets[0] or buff_num in cubes_sets[1] or buff_num in cubes_sets[2]:
                            return True
            elif len(buff_num) == 2:
                    inn = [[0, 0, 0], [0, 0, 0]]
                    for x, y in enumerate(list(buff_num)):
                            if y in buff_cubes[0]:
    				inn[x][0] = 1
    			elif y in buff_cubes[1]:
    				inn[x][0] = 1
    			elif len(buff_cubes) > 2 and y in buff_cubes[2]:
    				inn[x][0] = 1
    		if sum(myor(inn)) >= 2:
                            return True
            elif len(buff_num) == 3:
                    inn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    for x, y in enumerate(list(buff_num)):
                            if y in buff_cubes[0]:
    				inn[x][0] = 1
    			elif y in buff_cubes[1]:
    				inn[x][0] = 1
    			elif len(buff_cubes) > 2 and y in buff_cubes[2]:
    				inn[x][0] = 1
    		if sum(myor(inn)) == 3:
                            return True
            return False
    
def main():
            global cubes_sets
    	n = int(input())
    	cubes_sets = []
    	for x in range(n):
    		cubes_sets.append(set(input().split()))
    	lastn = 0
    	for x in range(1, 1000):
    		if can_make(x):
    			lastn = x
    			continue
    		else:
    			return lastn
    		
    				
    
    if __name__ == "__main__":
    	print(main())