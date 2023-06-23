def program3391():
    t = input()
    t = t.split(" ")
    a = int(t[0])
    b = int(t[1])
    if(a-b==1 || b-a==1):
    	print "Equal"
    elif(a > b):
    	print "Masha"
    else:
    	print "Dasha"
    