def program4908():
    input()
    l=map(int,input().split())
    a,b,c=sum(l[::3]),sum(l[1::3]),sum(l[2::3])
    if a>b:
     if a>c:
      print('chest')
      exit()
     print('back')
     exit()
    if b>c:
     print('biceps')
     exit()
    print('back')