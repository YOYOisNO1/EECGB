def program489():
    n,a,b,c=list(map(int,input().split()))
    l1=[a,b,c]
    l1.sort()
    ans=0
    if n%l1[0]==0:
        print(n//l1[0])
    else:
        if l1[0]!=l1[1]:
          for x in range(0,4001):
            for y in range(0,4001):
              z=(n-x*l1[0]-y*l1[1])/l1[2]
              if z<0:
                break
              if z==int(z):
                ans=max([ans,x+y+z])
          print(int(ans))
        else:
          for x in range(4001):
              z=(n-x*l1[0])/l1[2]
              if z<0:
                break
              if z==int(z):
                ans=max([ans,x+z])
          print(int(ans) 
          