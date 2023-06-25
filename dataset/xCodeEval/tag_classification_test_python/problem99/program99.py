def program99():
    x,y,z = map(int,input().split())
    a,b,c = map(int,input().split())
    if a>=x:
     a=a-x
     if y>a and (y-a)<=b:
        y-=a 
        a=0
        b-=y
     elif a>=y:
        a-=y
     elif y>a and (y-a)>=b:
         print("NO")
         z=100000000
     s= a+b+c    
     if s>=z:
          print("YES")
     elif z!=100000000:
          print("NO")
    else:
        print("NO")
    