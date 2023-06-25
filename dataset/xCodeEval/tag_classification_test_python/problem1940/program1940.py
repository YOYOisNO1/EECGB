def program1940():
    import sys
     
    input = sys.stdin.readline
     
    
    a,b = map(int,input().split())
    
    
    if (b-a==1):
        print(a*10+9,b*10)
    elif a==b:
        print(a*10,b*10+1)
    elif a==9 and b==1:
        print(99,100)
    else:
        print(-1)