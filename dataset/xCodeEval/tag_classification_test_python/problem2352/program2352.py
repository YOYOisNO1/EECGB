def program2352():
    n = int(input())
    
    count = 0
    rep = 2
    
    while n != 0:
      if n%2 == 0: 
        count_temp = n / 2
        n-=(2 * count_temp)
        count += count_temp
        continue
    
      while n % rep != 0 and rep * rep <= n:
        rep+=1
    
      if n % rep == 0:
        n-=rep
        count+=1
      else:
        n=0
        count+=1
        
    
    print(int(count))