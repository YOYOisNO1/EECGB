def program4271():
    n=int(input())
    print(n)
    prog=[]
    a=0
    for i in range(n):
      prog.append(int(input()))
    print(prog)
    d=prog[1]-prog[0]
    for i in range(n-1):
      if (prog[i+1]-prog[i])!=d:
        a=prog[n-1]
        break
    if a==0:
      a=prog[n-1]+d
    print(a)