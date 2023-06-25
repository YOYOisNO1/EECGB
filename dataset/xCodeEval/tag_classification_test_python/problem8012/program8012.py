def program8012():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 > x2 or y1 > y2) and x1 + y1 > max(x2, y2):
    	print("Vasiliy")
    else:
    	print("Polycarp")