def program4348():
    n=input()
    a=map(int,input().split(' '))
    diff=0
    l=[x for x in a if x>25]
    if len(l)==0:
      print(0)
    else:
      print(max(l)-25)