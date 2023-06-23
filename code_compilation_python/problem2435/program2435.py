def program2435():
    x=int(input())
    f=0
    for i in range(1,x+1):
         if (i*(i+1))//2==x:
              f=1
              break
    if f:
         print('YES')
    else:
    print('NO')
         
                   
    