def f(l1,r1,l2,r2,top):
      if top==0:
        return 0
      if (l1>r1 or l2>  r2):
        return 0
      if (l1>top):
        l1 -=top
        r1 -= top
      if (l2>top):
        l2-=top
        r2-=top
      #print(l1,r1,l2,r2,top)
    
      if ( (l1<= l2 and l2<= r1) or (l2<= l1 and l1<= r2)):
        ans =  min(r1,r2) -max(l1,l2)  +1
      else:
        ans = 0
      #print(ans)
      ans = max(ans, f(l1,min(r1,top-1),l2,min(r2,top-1), top//2))
      ans = max(ans, f(l1,min(r1,top-1),max(top+1,l2),r2, top//2))
      ans = max(ans, f(max(l1,top+1),r1, l2,min(r2,top-1), top//2))
      ans = max(ans, f(max(l1,top+1),r1, max(l2,top+1),r2, top//2))
    
      return ans
    
    a = input().split()
    
    
    print(f(int(a[0]),int(a[1]),int(a[2]),int(a[3]),2**30))