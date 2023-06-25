def program1302():
    n = int(input())
    s = input()
    k = 0
    
    for i in s:
        if i == 8:
            k++
            
    print(min(n // 11, k))