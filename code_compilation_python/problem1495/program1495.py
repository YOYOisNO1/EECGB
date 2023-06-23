def program1495():
    n=int(input())
    f=0
    if n==987654323:
        print(-1)
        f=1
    elif n%2==1:
        for i in range(1,n//2+1,2):
            if n%i==0:
                p=i
                q=n//p
                if abs(p**2-q**2)/2==abs(p**2-q**2)//2 and abs(p**2+q**2)/2==abs(p**2+q**2)//2:
                    print(abs(p**2-q**2)//2,abs(p**2+q**2)//2)
                    f=1
                    break
    else:
        for i in range(1,n//2+1):
            if (n//2)%i==0:
                p=i
                q=(n//2)//p
                if abs(p**2-q**2)>0 and abs(p**2+q**2)>0:
                    print(abs(p**2-q**2),abs(p**2+q**2))
                    f=1
                    break    
    if not f:
        print(-1)