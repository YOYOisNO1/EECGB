def program2994():
    a, b, c, n = map(int, input().split(' '))
    
    if c > a or c > b:
    	print(-1)
    else:
        pass_exam = a - c + b - c + c
    
    	if n - pass_exam > 0:
    		print(n - pass_exam)
    	else:
    		print(-1)