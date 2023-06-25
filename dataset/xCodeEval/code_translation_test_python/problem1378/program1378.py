def program1378():
    n = int(input())
    
    a = int(n ** 0.5)
    big_square = a ** 2
    
    else_square = n - big_square
    
    answer = int(a * 4)
    if a ** 2 != n:
        if else_square - a > 0:
            answer += 4
        else:
            answer += 2
    
    print(answer)