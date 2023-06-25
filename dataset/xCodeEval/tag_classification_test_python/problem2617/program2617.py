def program2617():
    import sys
    for integer in list(sys.stdin)[1]:
    	if integer == '1':
    		print('HARD')
    		break
    else: print('EASY')