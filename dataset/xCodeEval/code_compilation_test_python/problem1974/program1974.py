def program1974():
    n,pos,l,r=map(int,input().split())
    if l==1 and r==n:
      print(0)
    
    elif l==1 and r==pos or l==pos and r==n:
      print(1)
    elif pos==l and pos=a=r:
      print(2)
    elif l==1 and r<n and pos>=l and r>=pos:
      print(r-pos+1)
    elif l>1 and r==n and pos>=l and r>=pos:
      print(pos-l+1)
    elif pos>=l and r>=pos:
      count=0
      count=count+r-pos+1
      count=count+r-l+1
      a=count
      count=0
      count=count+pos-l+1
      count=count+r-l+1
      print(min(a,count))
    elif pos>r:
      count=0
      count=count+pos-r+1
      if l>1:
        count=count+r-l+1
      print(count)
    elif pos<l:
      count=0
      count=count+l-pos+1
      if r<n:
        count=count+r-l+1
      print(count)
    