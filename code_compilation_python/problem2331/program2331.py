def program2331():
    path = input()
    i = 0
    empty = None
    # empty input
    if len(path) == 0:
        empty = True
    	
    while i != len(path)-1 and not empty:
    	if path == '/':
            break
        
    	# search for '//' occurences
    	if path[i] == '/' and path[i+1] == '/':
            path = path[:i] + path[i+1:]
            i -= 1
        i += 1
    
    if 'root/' == path[-5:]:
        print(path)
    elif empty:
        print('')
    elif path == '/':
        print('/')
    elif path[-1] == '/':
        print(path[:-1])
    else:
        print(path)