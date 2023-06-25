def program2026():
    #lost array
    n , l ,r = map(int , input().split())
    if l==1 :
                print(n,end = " ")
                
    else :
                a = [1]*n
                x = 1
                for _ in range(l-1):
                            a.pop(0)
                            x= x*2
                            a.append(x)
                print(sum(a), end= " ")
    if r==n :
                r = ((2^^(n))-1)
                print(r)
    else:
                
                x= 2^^(r-1)
                a = [x]*n 
                x= 1
                for _ in range(r-1):
                            a.pop(0)
                            a.append(x)
                            x= x*2
                            
                            