    import sys
    
def iswin(r1,r2,wk,bk):
      m = False
       
      if r1 == bk or r2 == bk:
        return False
      
      #if wk == bk:
      #  return True
    
      #print r1, r2, wk, bk
      if r1[:1]==bk[:1]:
        lb = min(r1[1:],bk[1:])
        ub = max(r1[1:],bk[1:])
        if (r2[:1] != r1[:1] or r2[1:] < lb or r2[1:] > ub) and \
            (wk[:1] != r1[:1] or wk[1:] < lb or wk[1:] > ub):
          m = True
    
      if r1[1:]==bk[1:]:
        lb = min(r1[:1],bk[:1])
        ub = max(r1[:1],bk[:1])
        if (r2[1:] != r1[1:] or r2[:1] < lb or r2[:1] > ub) and \
            (wk[1:] != r1[1:] or wk[:1] < lb or wk[:1] > ub):
          m = True
    
      if r2[:1]==bk[:1]:
        lb = min(r2[1:],bk[1:])
        ub = max(r2[1:],bk[1:])
    
    if (r1[:1] != r2[:1] or r1[1:] < lb or r1[1:] > ub) and \
            (wk[:1] != r2[:1] or wk[1:] < lb or wk[1:] > ub):
          m = True
      
      if r2[1:]==bk[1:]:
        lb = min(r2[:1],bk[:1])
        ub = max(r2[:1],bk[:1])
        if (r1[1:] != r2[1:] or r1[:1] < lb or r1[:1] > ub) and \
            (wk[1:] != r2[1:] or wk[:1] < lb or wk[:1] > ub):
          m = True
    
      x1,y1 = map(ord,wk)
      x2,y2 = map(ord,bk)
      
      if abs(x1-x2)<=1 and abs(y1-y2)<=1:
        m = True
    
      return m
    
    r1, r2, wk, bk = sys.stdin.readline().strip().split(' ')
    mate = True
    
    if iswin(r1,r2,wk,bk)==False:
      mate = False
    
    if bk[:1] >'a':
      nbk = chr(ord(bk[:1])-1) + bk[1:]
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[:1] < 'h':
      nbk = chr(ord(bk[:1])+1) + bk[1:]
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[1:] > '1':
      nbk = bk[:1] + chr(ord(bk[1:])-1)
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[1:] < '8':
      nbk = bk[:1] + chr(ord(bk[1:])+1)
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[:1] > 'a' and bk[1:] > '1':
      nbk = chr(ord(bk[:1])-1) + chr(ord(bk[1:])-1)
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[:1] > 'a' and bk[1:] < '8':
      nbk = chr(ord(bk[:1])-1) + chr(ord(bk[1:])+1)
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[:1] < 'h'and bk[1:] > '1':
      nbk = chr(ord(bk[:1])+1) + chr(ord(bk[1:])-1)
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if bk[:1] < 'h' and bk[1:] < '8':
      nbk = chr(ord(bk[:1])+1) + chr(ord(bk[1:])+1)
      if iswin(r1,r2,wk,nbk) == False:
        mate = False
    
    if mate:
      print 'CHECKMATE'
    else:
      print 'OTHER'
    