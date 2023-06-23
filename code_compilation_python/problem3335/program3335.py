def program3335():
    x=int(input())
    z=[n for n in str(int(input()))]
    l=0
    for n in z:
      in n!=4 or n!=7:
        print('NO')
        l=0
        break
      else:
        l=1
    if l==1:
      if sum(z[0::x//2])==sum(z[x//2:x])
        print('YES')
      else:
        print('NO')
    