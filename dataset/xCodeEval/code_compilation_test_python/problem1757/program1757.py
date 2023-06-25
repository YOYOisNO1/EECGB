def program1757():
    s = input()
    t = input()
    p = ""
    h = 0 
    m = 0
    
    if(int(s.split(':')[0]) < int(t.split(':')[0])):
    	h = int(s.split(':')[0]) + 24 - int(t.split(':')[0])
    else:
    	h = int(s.split(':')[0]) - int(t.split(':')[0])
    if(int(s.split(':')[1]) < int(t.split(':')[1])):
        if(int(s.split(':')[0]) == int(t.split(':')[0])):
    	    h = int(s.split(':')[0])
    	m = int(s.split(':')[1]) + 60 - int(t.split(':')[1])
    else:
    	m = int(s.split(':')[1]) - int(t.split(':')[1])
     
    if(h < 10):
    	p = "0" + str(h)
    else:
    	p = str(h)
    if(m < 10):
    	p += ":0" + str(m)
    else:
    	p += ":" + str(m)
     
    print(p)