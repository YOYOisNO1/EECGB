def program4540():
    x = int(input().strip())
    ab, cd = map(int, input().strip().split())
    count = 0
    while ab%10 != 7 and cd%10 != 7:
    	if cd >= x:
    		cd -= x
    	else:
    		ab = (ab - 1)%24
    		cd = cd + 60 - x
    	count += 1
    print(count)