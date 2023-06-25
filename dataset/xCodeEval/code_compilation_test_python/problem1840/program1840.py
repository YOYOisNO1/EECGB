def program1840():
     n, k, l, c, d, p, nl, np = map(int,input().split())
     line = []
     every1 = k*l / nl
     every2 = c*d
     every3 = p/np
     line.append(every1)
     line.append(every2)
     line.append(every3)
    
     line = sorted(line)
    
     print line[0]/n
    