def program2148():
    #for _ in range(int(input(''))):
    n=int(input('')) 
    #n,k=map(int, input().split())
    #a=list(map(int, input().split()))
    #c=a.count(1)
    #print('YES')
    k=n%4
    if k==1:
      print('0 A')
    elif k==0:
      print('1 A')  
    elif k==2 :
      print('1 B')
    elif k==3:
      print('2 A')  
     