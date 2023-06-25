def program2654():
    a , b= map(int , input().split())
    c =0 
    while b : #  when b will be zero  the loop will be stop 
        c+=a//b
        a, b = b , a%b 
           
    print(c)