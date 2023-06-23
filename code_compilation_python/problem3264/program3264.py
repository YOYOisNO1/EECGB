    import sys
    
def main(argv):
    	num = int(input())
    
    	if num < 2:
    		print "-1"
    		sys.exit()
    
    	points = list()
    	for x in xrange(num):
    		pos = [int(item) for item in input().split(' ')]
    		points.append(pos)
    
    	if num == 2:
    		if points[0][0] == points[1][0] or points[0][1] == points[1][1]:
    			print "-1"
    			sys.exit()
    
    	len1 = 0
    	len2 = 0
    	index = 0
    	while len1 == 0 or len2 == 0:
    		if points[index][0] != points[index + 1][0]:
    			len1 = abs(points[index][0] - points[index + 1][0])
    
    		if points[index][1] != points[index + 1][1]:
    			len2 = abs(points[index][1] - points[index + 1][1])
    
    	print repr(len1 * len2)
    
    
    if __name__ == "__main__":
    	main(sys.argv)