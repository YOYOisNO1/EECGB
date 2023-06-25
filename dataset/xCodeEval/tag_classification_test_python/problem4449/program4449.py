def program4449():
    a=input().strip()
    a=a.replace('at','@')
    a=a.replace('dot','.')
    a=list(a)
    if a[0]=='.':
      a[0]='dot'
    if a[-1]=='.':
      a[-1]='dot'
    if a[0]=='@':
      a[0]='at'
    f=0
    for i in range(len(a)):
      if a[i]=='@' and f==0:
        f=1
      elif a[i]=='@' and f==1:
        a[i]='at'
    print(''.join(a))