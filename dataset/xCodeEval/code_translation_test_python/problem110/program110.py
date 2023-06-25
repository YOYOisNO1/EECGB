def program110():
    n = int(input())
    
    sum = 1
    
    for i in range(1, n):
        sum = sum + 4 * i
        
    print(sum)