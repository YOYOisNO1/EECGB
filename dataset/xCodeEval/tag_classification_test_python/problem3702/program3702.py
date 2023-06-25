def program3702():
    a=input()
    for i in xrange(len(a)): 
      if a[len(a)-i-1]!='0':
        a=a[:len(a)-i]
        break
    if a==a[::-1]:
      print('YES')
    else:
      print("NO")