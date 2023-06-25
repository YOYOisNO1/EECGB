def program203():
    x = str(input())
    list=[0,0]
    i = 0
    while i<len(x):
      if x[i]=="o":
        list[0]=list[0]+1
      else:
        list[1]=list[1]+1
      i+=1  
    if list[0]==0 or list[1]==0 :
      print("YES")
    elif list[1]%list[0] ==0:
      print("YES")
    else:
      print("NO")
      
      
    