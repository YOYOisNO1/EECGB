def program3761():
    n = int(input())
    a = [int(i) for i in input().split()]
    if len(a) > 1:
    	if a[n - 1] == 15:
    		print("DOWN")
    	elif a[n - 1] - a[n - 2] >= 0:
    		print("UP")
    	elif a[n-1] == 0:
    		print("UP")
    	else:
    		print("DOWN")
    elif a[n - 1] == 15:
        print("DOWN")
    elif a[n - 1] == 0:
        print("UP")
    else:
    	print(-1)