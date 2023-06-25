def program1609():
    ss =list(input().strip())
    j= {'H': True, 'Q': True, '9': True}
    for k in ss:
    	if k in j:
    		print("YES")
    		break
    else:
        print("NO")
        