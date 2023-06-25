def gcd(a, b) :
      while a != 0 and b != 0 :
        if a > b :
          return gcd (a % b, b)
        else :
          return (gcd(b % a, a))
      return (a + b)
    
    n = int(input())
    b = [0] * n
    ans = 0
    b = [int (i) for i in input().split()]
    b.sort()
    for i in range(n):
      if b[i] != -1 :
        for j in range(i + 1, n):
          if (gcd(b[i], b[j]) > 1) :
            b[j]  = -1
            #print (b)
    for i in b:
      if i != -1 && i != 1:
        ans += 1
    print (b)
    print (ans)