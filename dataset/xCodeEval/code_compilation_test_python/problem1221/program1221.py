def program1221():
    ﻿a=input()
    b=input()
    
    if a=='monday':
    	if b=='monday' or b=='wednesday' or b=='thursday':
    		print('YES')
    	else:
    		print('NO')
    if a=='tuesday':
    	if b=='tuesday' or b=='thursday' or b=='friday':
    		print('YES')
    	else:
    		print('NO')
    if a=='wednesday':
    	if b=='wednesday' or b=='friday' or b=='saturday':
    		print('YES')
    	else:
    		print('NO')
    if a=='thursday':
    	if b=='thursday' or b=='saturday' or b=='sunday':
    		print('YES')
    	else:
    		print('NO')
    if a=='friday':
    	if b=='friday' or b=='sunday' or b=='monday':
    		print('YES')
    	else:
    		print('NO')
    if a=='saturday':
    	if b=='saturday' or b=='monday' or b=='tuesday':
    		print('YES')
    	else:
    		print('NO')
    if a=='sunday':
    	if b=='sunday' or b=='tuesday' or b=='wednesday':
    		print('YES')
    	else:
    		print('NO')