def program2754():
    a=input().split(':')
    while 1:
     a=list(map(int,a))
     a[1]+=1
     if a[1]==60:a[0],a[1]=a[0]+1,a[1]-60
     if a[0]==24:a[0]-=24
     a=list(map(str,a))
     for i in [0,1]:
      if len(a[i])==1:a[i]='0'+a[i]
     if a[0]=a[1][::-1]:break
    print(':'.join(a))