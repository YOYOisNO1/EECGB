def program2335():
    import sys
    
    
    
    n,k=map(int,input().split())
    a=map(int,input().split())
    
    w=0 
    for x in range(n/k):
       een=0
       twee=0
       for y in range (n/k):
          if a[x+y*k]==1:
             een+=1
          else:
             twee+=1
       w+=min(een,twee)
          
    print w
    
        