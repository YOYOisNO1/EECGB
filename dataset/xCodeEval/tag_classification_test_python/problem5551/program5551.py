    ((x,y,r,R),(u,v,w,W))=[map(int,input().split()) for _ in (1,2)]
    d=(x-u)*(x-u)+(y-v)*(y-v)
def t(a,b,c):
      if c<=a and (a-c)*(a-c)>=d:return 1
      if c>=b and (c-b)*(c-b)>=d:return 1
      if (b+c)*(b+c)<=d:return 1
      return 0
    print(t(r,R,w)+t(r,R,W)+t(w,W,r)+t(w,W,R))
    