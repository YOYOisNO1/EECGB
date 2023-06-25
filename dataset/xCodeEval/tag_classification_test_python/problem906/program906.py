def program906():
    from itertools import combinations as C
    v=map(int,input())
    n=len(v)
    N=range(n)
    for w in range(1,4):
      for t in C(range(n),w):
        x=[0,0,0]+[v[i] for i in t]
        y=x[-3]*100+x[-2]*10+x[-1]
        if not y%8:
          print('YES')
          print(y)
          exit(0)
    print('NO')