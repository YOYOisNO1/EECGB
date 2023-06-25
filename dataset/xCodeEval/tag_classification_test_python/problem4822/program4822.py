def program4822():
    
    inp = map(int, input().split())
    l = inp[0]
    r = inp[1]
    
    res=0
    
    for x in xrange(0,32):
      for y in xrange(0,32):
        z=pow(2,x)*pow(3,y)
        if(l<=z and z<=r):
          res+=1
    
    print(res)