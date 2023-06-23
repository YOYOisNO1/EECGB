def program2275():
    a = list(input())
    c=0
    mid = len(a)//2
    
    for i in range(mid):
       if a[i]==a[-(i+1)]:
           pass
       else:
           c+=1
    
    if c=1:
        print('YES')
    else:
        print('NO')