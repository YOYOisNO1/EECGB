def program6169():
    r1, c1, r2, c2 = map(int,input().split())
    
    if r1 == r2 or c1 == c2 :
      rook = 1
    else :
      rook = 2
    
    t1 = (r1+c1)%2
    t2 = (r2+c2)%2  
    if t2 == t1 :
      if abs(r1-r2) == abs(c1 - c2) :
        bishop = 1
      else :
        bishop = 2
    else :
      bishop = 0
    
    if r1 == r2 :
      king = abs(c1-c2)
    elif c1 == c2 :
      king = abs(r1 - r2)
    elif  abs(r1-r2) == abs(c1 - c2) :
      king = abs(r1 - r2)
    else : 
      king = max(abs(r1 - r2),abs(c2-c1))
         
    print(rook,bishop,king)