def program474():
    #732A
    k,r = list(map(int, input().split()))
    t = 1
    t1 = 1
    while (((t * 10) + r) % k) != 0:
      t = t + 1
    print ((((t1 * 10) + r) // k))
    
    if t1 < t:
      print((((t1 * 10) + r) / k))
    else 
      print((((t1 * 10)) / k))
      