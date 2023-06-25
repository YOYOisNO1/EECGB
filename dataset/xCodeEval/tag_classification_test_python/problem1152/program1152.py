def program1152():
    t = int(input())
    s = int(input())
    v = int(input())
    j = int(input())
    e = int(input())
    f = int(input())
    
    pro = 0
    
    if j == t+min(s, v):
    	pro += e*t + f*min(s,v)
    elif e > f:
    	to = min(j, t)
    	pro += e*to
    	j -= to
    	pro += f*min(j, min(s, v))
    elif e < f:
    	to = min(j, min(s, v))
    	pro += f*to
    	j -= to
    	pro += e*min(j,t)
    elif e == f:
    	pro += min(j, t+min(s, v))*e
    print(pro)