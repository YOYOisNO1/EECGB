def program540():
    x=input()
    z=[]
    for i in range(int(x)):
      z.append(input())
    first="1"
    second="2"
    spect="3"
    flag=True
    for i in range(int(x)):
      if z[i]==first:
        temp=second
        second=spect
        spect=temp
        
      elif z[i]==second:
        temp=first
        first=spect
        spect=temp
      else:
        flag=False
        break
    
    if flag==True :
        print("YES")
    else:
        print("NO")