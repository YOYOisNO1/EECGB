def sum_digits(n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
    
    
    number_str = input()
    number = int(number_str)
    max_sum = sum_digits(number)
    result = number
    
    for i in range(len(number_str) - 1, -1, -1):
        number -= int(int(number_str[i]) + 1) * pow(10, len(number_str)-(i+1))
        number_str = str(number)
        if number < 0:
            break
        cur_sum = sum_digits(number)
        if cur_sum > max_sum:
            max_sum = cur_sum
            result = number
    
    print(result)