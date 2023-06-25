def program3384():
    a, b=  (input().split())
    
    a = int ( a)
    b = int (b)
    
    a = (a//b)
    #print(int (a))
    if( int (a % 2) == 1):
        print("YES")
    else: print("NO")