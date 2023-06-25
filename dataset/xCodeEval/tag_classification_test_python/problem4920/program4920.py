    n,m=map(int,input().split())
    lst=map(int,input().split())
    ans=[]
    #Generate All Subsequence Sum for a Array 
def r(lst,i,e,s=0):
      if i==e:
        ans.append(s%m)
      #s=s+lst[0]
    
      #ans.append(s)
      else:
        r(lst,i+1,e,s)
        r(lst,i+1,e,s+lst[i])
    if len(lst)>0:
      q=n/2
      l1=lst[0:q]
      l2=lst[q:]
      r(l1,0,q)
      a1=ans
      ans=[]
      r(l2,0,len(l2))
      a2=ans 
    a1.sort()
    a2.sort()
    from bisect import *
    import bisect
    k=0
    ans=[]
    mk=-100
    for i in a1:
      val=i
      val=((val+a2[(bisect_left(a2,m-val)-1)])%m)
      if val>mk:
        mk=val
    print(mk)
    