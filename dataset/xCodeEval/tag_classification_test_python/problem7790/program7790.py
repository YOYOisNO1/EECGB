    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[1,1,0,-1,-1,-1,0,1]
def go(d,v):
      t={}
      if v:
        h=v.pop()
        s=go((d+1)%8,v)
        d1=(d+1)%8
        x,y=-dx[d1],-dy[d1]
        for _ in range(h):
          s[(x,y)]=1
          x-=dx[d]
          y-=dy[d]
        x+=dx[d]
        y+=dy[d]
        for u,v in s:
          u-=x
          v-=y
          t[(u,v)]=1
          p,q=dx[d],dy[d]
          r=p*q
          u,v=(-u,v) if 0==p else (u,-v) if 0==q else (v*r,u*r)
          t[(u,v)]=1
      return t
    input()
    print(len(go(0,map(int,input().split())[::-1])))