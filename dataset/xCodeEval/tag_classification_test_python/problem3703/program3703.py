def program3703():
    num = input()
    count_ends_zero = 0
    result = "NO"
    for i in num[::-1]:
        if i == "0":
            count_ends_zero += 1
        else:
            break
    for i in range(count_ends_zero+1):
        if ("0"*i+num) == ("0"*i+num)[::-1]:
            result = "YES"
            break
    print(result)