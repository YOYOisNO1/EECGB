def program2708():
    n = int(input())
     
    s = map(int,input().split())
     
    k = max(s)
    som = 0
    for i in s:
      som+=i
     
     
    while som>=((k*n) - som):
      k+=1
    print k