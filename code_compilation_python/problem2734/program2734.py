def program2734():
    l=[]
    for i in range(11):
          l.append(input())
          if "x" in l[i]:
    x,y=map(int,input().split())
    if x>=4 and x<=6:
          x-=3
    elif x>=7:
          x-=6
    if y>=4 and y<=6:
          y-=3
    elif y>=7:
          y-=6
    if x==1:
          p=0
    elif x==2:
          p=4
    elif x==3:
          p=8     
    if y==1:
          p2=0
    elif y==2:
          p2=4
    elif y==3:
          p2=8
    com=0
    for i in range(p,p+3):
          for j in range(p2,p2+3):
                if l[i][j]=='.':
                      com+=1
    if com==0:
          for i in (0,1,2,4,5,6,8,9,10):
                if i ==4 or i==8:
                      print()
                for j in range(11):
                      if l[i][j]=='.':
                            print("!",end="")
                      else:
                            print(l[i][j],end="")
                print()
    else:
          for i in (0,1,2,4,5,6,8,9,10):
                if i==4  or i==8:
                      print()
                for j in range(11):
                      if i>=p and i < p+3 and j >= p2 and j < p2+3:
                            if l[i][j]=='.':
                                  print("!",end="")
                            else:
                                  print(l[i][j],end="")
                      else:
                            print(l[i][j],end="")
                print()
                