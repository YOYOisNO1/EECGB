def is_right(coords):
    	x1, y1, x2, y2, x3, y3 = coords
    
    	sl12 = (x1 - x2)**2 + (y1 - y2)**2
    	sl13 = (x1 - x3)**2 + (y1 - y3)**2
    	sl23 = (x2 - x3)**2 + (y2 - y3)**2
    
    	return sl12 != 0 and sl13 != 0 and sl23 != 0 and (
    		sl12 == sl13 + sl23 or
    		sl13 == sl12 + sl23 or
    		sl23 == sl12 + sl13
    	)
    
    
def main():
    	coords = list(map(int, input().strip().split()))
    
    	if is_right(coords):
    		print('RIGHT')
    		return
    
    	for i in range(6):
    		ori = coords[i]
    
    		coords[i] = ori + 1
    		if is_right(coords):
    			print('ALMOST')
    			return
    
    		coords[i] = ori - 1
    		if is_right(coords):
    			print('ALMOST')
    			return
    
    		coords[i] = ori
    
    	print('NEITHER')
    if __name__ == '__main__':
    	main()