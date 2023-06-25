def program1179():
    n,x,y = map(int, input().split(" "))
    
    if n < 3 or (x==n/2 and y==n/2 or x==n/2 and y==n/2+1 or x==n/2+1 and y==n/2 or x==n/2+1 and y==n/2+1 ):    print("NO")
    else:   print("YES")