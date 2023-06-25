    dx=[0,1,1,1,0,-1,-1,-1]*4
    dy=[1,1,0,-1,-1,-1,0,1]*4
def go(d,v):
      t={}
      if v:
        h=v.pop()
        s=go(d+1,v)
        x,y=-dx[d+1],-dy[d+1]
        for _ in range(h):
          s[(x,y)]=1
          x-=dx[d]
          y-=dy[d]
        p,q=dx[d],dy[d]
        r=p*q
        x+=p
        y+=q
        for u,v in s:
          u-=x
          v-=y
          t[(u,v)]=1
          u,v=(-u,v) if 0==p else (u,-v) if 0==q else (v*r,u*r)
          t[(u,v)]=1
      return t
    input()
    print(len(go(0,map(int,input().split())[::-1])))
    # print(go(0,map(int,input().split())[::-1]).keys())