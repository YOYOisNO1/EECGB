def program3259():
    import fractions
    import sys
    import math
    
    toks = sys.stdin.readline().split()
    t1 = int(toks[0])
    t2 = int(toks[1])
    y1max = int(toks[2])
    y2max = int(toks[3])
    t0 = int(toks[4])
    
    dt1 = t0 - t1
    dt2 = t2 - t0
    
    if dt1>0:
      calc1max = (y2max * dt2) / dt1
      if calc1max<y1max: y1max = calc1max
    
    if   dt1==0 and dt2==0: y1out,y2out = y1max,y2max
    elif dt1==0: y1out,y2out = y1max,0
    elif dt2==0: y1out,y2out = 0,y2max
    elif y1max<=1:
      if float(t2*y2max+t1)/(y2max+1) < t0:
        y1out,y2out=0,y2max
      else:
        y1out,y2out=1,y2max
        y2 = y2out
        errMin = (1*t1 + y2*t2) / float( 1+y2) - t0
        while y2>1:
          y2 -= 1
          err = (1*t1 + y2*t2) / float( 1+y2)
          if err<0.0: break
          if err<errMin: continue
            y2out = y2
            if err==0.0: break
            errMin = err
       
    else:
    
      fy1max = float(y1max)
      fy2max = float(y2max)
      y2 = y2max
      y1 = (y2 * dt2) / dt1
      if y1>y1max:
        y2 = (y1max * dt1 + dt2 - dt2) / dt2
      y1 = (y2 * dt2) / dt1
    
      g = fractions.gcd( dt1, dt2)
      if g > 1:
        dt1 /= g
        dt2 /= g
    
      minErr = (float( y2 * t2 + y1 * t1 ) / (y1+y2)) - t0
    
      rem1 = y1 % dt2
      rem2 = y2 % dt1
      y11, y12, y21, y22 = y1, y1, y2, y2
      err1, err2 = minErr,minErr
    
      if rem1<y11 or y11==0:
        y11 -= rem1
        y21 = (y11 * dt1) / dt2
        err1 = (float( t2 * y21 + t1 * y11 ) / (y1+y2)) - t0
    
      if rem2<y22:
        y22 -= rem2
        y12 = (y22 * dt2) / dt1
        err2 = (float( t2 * y22 + t1 * y12 ) / (y1+y2)) - t0
    
      if err1==0 and err2==0: y1out,y2out = max(y11,y12),max(y21,y22)
      elif err1==0: y1out,y2out = y11,y21
      elif err2==0: y1out,y2out = y12,y22
      else:
        if err1<err2: minErr,y1out,y2out = err1, y11, y21
        else        : minErr,y1out,y2out = err2, y12, y22
    
        while y2>1:
          y2-=1
          y1 = (y2 * dt2) / dt1
          err = (float( y2*t2 + y1*t1 ) / (y1+y2)) - t0
          if err<minErr:
            minErr,y1out,y2out = err, y1, y2
      
      
    print( "%d %d" % (y1out,y2out,) )