def program817():
    n = int(input())
    s = "ROYGBIV"
    
    for i in range(n-7):
        s += s[-4]
        
    print(s)
    