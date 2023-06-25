def program5810():
    a,b,x,y=map(int,input().split())
    l,h=0,1<<50
    xy=x*y
    while l<h:
     v=(l+h)/2
     if v-v/x<a or v-v/y-max(0,a-v/y+v/xy)<b:l=v+1
     else:h=v
    print(l)
    