def program157():
    sequence = list(input())
    x = sequence[0]
    y = 1
    numbers = []
    
    i = 0
    while i <= (len(sequence) - 1):
    	if sequence[i + 1] == x:
    		y += 1
    	else:
    		x = sequence[i + 1]
    		numbers.append(y)
    		y = 1
    
    if max(numbers) >= 7:
    	print 'YES'
    else:
    	print 'NO'
    	