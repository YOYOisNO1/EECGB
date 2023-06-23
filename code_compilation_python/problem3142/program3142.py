def b(n):
      ans = [n]
      for x in xrange(2, n):
        while n % x == 0:
          n /= x
          ans.append(n)
      return ' '.join(map(str, ans))
    
    
    """
    print b(10)
    print b(4)
    print b(3)
    """
    print b(int(input())
    #"""