def program3789():
    By kudlacz964, contest: Lyft Level 5 Challenge 2018 - Final Round (Open Div. 2), problem: (A) The King's Race, Wrong answer on test 34, #
     import math
    
    n = int(input())
    x, y = map(int, input().split(" "))
    
    white = math.sqrt((x - 1) * (x - 1) + (y - 1) * (y - 1))
    black = math.sqrt((x - n) * (x - n) + (y - n) * (y - n))
    
    if white == black:
    	if x > int(n / 2) and y > int(n / 2):
    		print("Black")
    	else:
    		print("White")
    elif white < black:
    	print("White")
    else:
    	print("Black")