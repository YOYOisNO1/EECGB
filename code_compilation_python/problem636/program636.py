def program636():
     n , m = map(int , input().split())
        s = n # s refers sum 
        while n >= m :
            n = n%m + n//m 
            s+=n 
        print(s)