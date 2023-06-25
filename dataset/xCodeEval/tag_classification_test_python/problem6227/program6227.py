def program6227():
    x,y = map(int, input().split())
    d = None
    if x < y:
    	d = ['Dasha', 'Masha']
    else:
    	x,y = y,x
    	d = ['Masha', 'Dasha']
    Yscore = 0
    for i in range(y, x * y + 1, y):
    	Yscore += (i - (((i - 1)// x) * x))
    Xscore = x * y - Yscore
    if Xscore > Yscore:
    	print(d[0])
    elif Xscore < Yscore:
    	print(d[1])
    else:
    	print('Equal')