def program4714():
    if __name__ == '__main__':
    	n , k = [int(x) for x in input().split()]
    	guests = input()
    	goin = {}
    	size = 0
    	last = {}
    	# for guest in guests:
    	# 	if guest not in numget:
    	# 		numget[guest] = 1
    	# 	else:
    	# 		numget[guest] += 1
    	# for guest in guest:
    	# 	if guest not in dic:
    	# 		dic[guest] = 1
    	# 		check += 1
    	# 	else:
    	# 		dic[guest] += 1
    	# 		check += 1
    	# 	if check > k:
    	# 		print('YES')
    	# 		return
    	# 	if dic[guest] == numget[guest]:
    	# 		check -= 1 
    
    	check = 0
    	for i in range(n):
    		last[guests[i]] = i
    		goin[guests[i]] = 0
    	for i in range(n):
    		if not goin[guests[i]]:
    			goin[guests[i]] = 1
    			size += 1
    		if size > k:
    			print('YES')
    			check = 1
    			break
    		if i == last[guests[i]]:
    			size -= 1
    	if check == 0:
    		print('NO')