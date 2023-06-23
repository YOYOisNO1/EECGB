def sum_numbers(numb):
        sum = 0
        while numb:
            sum += numb % 10
            numb //= 10
    
        return sum
    
    n = int(input())
    
    ans, cap = n, 10
    
    for i in range(len(str(n)) - 1):
        new_n = (n // cap - 1)
        for j in range(len(str(cap)) - 1):
            new_n = new_n * 10 + 9
        
        if sum_numbers(n) >= sum_numbers(new_n) && sum_numbers(n) >= sum_numbers(ans):
            ans = n
        elif sum_numbers(new_n) >= sum_numbers(ans):
            ans = new_n
        cap *= 10
    
    print(ans)
    