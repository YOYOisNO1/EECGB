def program864():
    # C. Vasya and Golden Ticket
    
    n = int(input())
    digits = list(input())
    digits = list(map(int, digits))
    dig_sum = sum(digits)
    part_sum = 1
    if dig_sum == 0:
        print("YES\n")
        exit()
    # 由于数据量不大，因此枚举每一种可能的部分和
    for part_sum in range(1, dig_sum):      # 用for比 while代码量更小，占内存也更小
        if dig_sum % part_sum != 0:
            continue
        temp = 0                            # 注意要置零！！
        for i in range(0, n):               # i就不需要再置零了，每次都会从range的第一个开始
            temp += digits[i]
            if temp == part_sum:            # 这里不需要再开一个flag，直接用temp就很方便
                temp = 0
            elif temp > part_sum:
                break
        if temp == 0:
            print("YES\n")
            exit()
    print("NO\n")