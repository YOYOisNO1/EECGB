    class var:
      p=0
      r=0
    s1=var()
    arr=[]
    n=200001
    for i in range(0,n):
      c=var()
      c.p=i
      arr.append(c)
def find(i):
      if arr[i].p!=i:
        arr[i].p=find(arr[i].p)
      return arr[i].p
def union(a,b):
      xr=find(a)
      yr=find(b)
      if arr[xr].r<arr[yr].r:
        arr[xr].p=yr
        arr[yr].r+=1
      elif arr[xr].r>arr[yr].r:
        arr[yr].p=xr
        arr[xr].r+=1
      else:
        arr[yr].p=xr
        arr[xr].r+=1
      #for i in arr:
        #print(i.p,i.r)
      #print("hi")
    n=input()
    k=input()
    for _ in range(0,k):
        a,b=map(int,input().split())
        union(a,b)
    ans=[]
    for i in range(0,n+2):
      l2=[]
      ans.append(l2)
    for i in range(1,n+1):
      val=find(i)
      ans[val].append(i)
    #print(ans)
    
    t=input()
    z=[]
    for _ in range(0,t):
        a,b=map(int,input().split())
        z.append((a,b))
    from collections import *
    fv=[0]
    for i in ans:
    
        if len(i)>0:
            ans=0
            ck=Counter(i)
            for j in z:
                if j[0] in ck and j[1] in ck:
                    ans=-1
                    break
            if ans==0:
                fv.append(len(i))
    print(max(fv))