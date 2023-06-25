def program1132():
    from sys import stdin
    
    a , b = map(int,stdin.readline().split())
    x = 6 - max(a,b)
    arr = ["1/6","1/3","1/2","2/3","5/6","1/1"]
    
    print(arr[x])