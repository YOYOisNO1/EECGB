def program30():
    n = int(input())
    l = [4,7,47,74,447,474,477,747,774]
    i = 0 
    while i < len(l) and l[i] <= n :
      if n % l[i] == 0:
        print 'YES' 
        i =+ 1
        break
    if i == len(l):
      print 'NO'