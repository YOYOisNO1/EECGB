def program2371():
    num = int(input())
    
    count = 0
    while num != 0:
        lst = [int(i) for i in str(num)]
        num -= max(lst)
        count += 1
    
    return count