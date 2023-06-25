def cal(ar,cnt):
      if ar[0]==ar[1]:
       return cnt+ar[0]
      elif ar[0]==ar[2]:
       return cnt+ar[0]
      elif ar[1]==ar[2]:
       return cnt+ar[1]
      else:
       ar.sort()
       ar[2]-=1
       ar[1]-=1
       ar[0]+=1
       cnt+=1
       return cal(ar,cnt)
    
    a = list(map(int,input().split()))
    print(cal(a,0))