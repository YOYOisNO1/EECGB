def program3692():
    d={input():0}
    for i in range(50,0,-1):
     d,e={},d
     u=10**i/9
     for v,c in e.items():
      for x in range(-6,7):
    	t=x*u+v
    	if abs(t)<u:d[t]=min(c+i*abs(x),d.get(t,99999))
    print d[0]