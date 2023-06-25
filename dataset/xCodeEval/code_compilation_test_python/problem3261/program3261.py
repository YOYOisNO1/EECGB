def program3261():
    n = int(input())
    if n == 1:
    	x1, y1 = map(int, input().split())
    	print(-1)
    elif n == 2:
    	x1, y1 = map(int, input().split())
    	x2, y2 = map(int, input().split())
    	if (max(x2, x1) - min(x1, x2)) * (max(y1, y2) - min(y1, y2)) > 0:
    		print((max(x2, x1) - min(x1, x2)) * (max(y1, y2) - min(y1, y2)))
    	else:
    		print(-1)
    elif n == 3:
    	x1, y1 = map(int, input().split())
    	x2, y2 = map(int, input().split())
    	x3, y3 = map(int, input().split())
    	if (max(x3, x2, x1) - min(x1, x2, x3)) * (max(y1, y2, y3) - min(y1, y2, y3)) > 0:
                    print((max(x2, x1, x3) - min(x1, x2, x3)) * (max(y1, y2, y3) - min(y1, y2, y3)))
    	else:
    		print(-1)
    elif n == 4:
            x1, y1 = map(int, input().split())
            x2, y2 = map(int, input().split())
            x3, y3 = map(int, input().split())
    	x4, y4 = map(int, input().split())
            if (max(x3, x2, x1, x4) - min(x1, x2, x3, x4)) * (max(y1, y2, y3, y4) - min(y1, y2, y3, y4)) > 0:
                    print((max(x2, x1, x3, x4) - min(x1, x2, x3, x4)) * (max(y1, y2, y3, y4) - min(y1, y2, y3, y4)))
            else:
                    print(-1)