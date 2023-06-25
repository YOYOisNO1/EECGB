def program5168():
    import math
    n,l,r = [int(e) for e in input().split()]
    
    mylist = [n]
    
    curl = 1
    curr = 2**math.ceil(math.log(max(n,1)+1,2))-1
    
    while curl<l:
      #print(curl,mylist)
      x = mylist[0]
      if x>1:
          mylist = mylist[1:]
          mylist = [x//2,x%2,x//2] + mylist
      while curl+2**math.ceil(math.log(max(mylist[0],1)+1,2))-1<=l:
        curl += 2**math.ceil(math.log(max(mylist[0],1)+1,2))-1
        mylist = mylist[1:]
    #print(curl,mylist)
    #print("-")
    
    while curr>r:
      #print(curr,mylist)
      x = mylist[-1]
      if x>1:
          mylist = mylist[:-1]
          mylist += [x//2,x%2,x//2]
      while curr-2**math.ceil(math.log(max(mylist[-1],1)+1,2))+1>=r:
        curr -= 2**math.ceil(math.log(max(mylist[-1],1)+1,2))-1
        mylist = mylist[:-1]
    #print(curr,mylist)
        
    print(sum(mylist))
      