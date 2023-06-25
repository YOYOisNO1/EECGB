    n = int(input())
    
def a(n):
      if n == 0:
        return 1
      return 2*(2*n+1)*a(n-1)/(n+1) 
    
def c(n):
      return 2 * a(n-1) - n
    
    #for x in range(1, 10):
    #  print x, c(x)
    
    print c(n)
    