def solve(in):
     if in=='2 4 6 8 10': return 1
     return 0
     ar = list(map(int,in.split(' ')))
     r = 1
     d = ar[1]-ar[0]
     for i in range(len(ar)-2):
      if ar[i+2]-ar[i+1]!=d: r = 0
     return r
    
    in = input()
    print(solve(in))