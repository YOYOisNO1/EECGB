def program3503():
    x=input()
    y=input()
    a=60*int(x[:2])+int(x[3:])
    b=60*int(y[:2])+int(y[3:])
    a=(a+b)/2
    x=str(a/60)
    y=str(a-(a/60)*60)
    if len(x)<2:
    	x='0'+x
    if len(y)<2:
    	y='0'+y
    print(x+':'+y)