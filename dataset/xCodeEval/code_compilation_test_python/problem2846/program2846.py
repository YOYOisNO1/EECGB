def process(n):
      prev = 0
      curr = n
      int count = 0
      while not (prev==0 and curr==1):
        next = curr/2
        curr = n%2
        prev = curr
        curr = next
        count += 1
        if prev==1:
          next = 1
          curr -= 1
          prev = curr
          curr = next
          count += 1
      return count
    
    print process(int(input()))