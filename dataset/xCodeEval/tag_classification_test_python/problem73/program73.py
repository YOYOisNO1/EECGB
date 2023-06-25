def program73():
    n = int(input())
    
    a = [0] * (101)
    
    for i in list(map(int, input().split())):
        a[i] += 1
    
    print(max(a))