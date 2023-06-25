def Next(num):
        num = int(num)
        result = str(num + 1)
        #print(result, result[len(result)-1])
        while result[len(result)-1] == '0':
            result = result[:-1]
            #print(result, result[len(result)-1])
        return result
    
    num = input ()
    count = 1
    while True:
        if len(num) == 1:
            if num == '0':
                count = 10
                break
            else:
                count = 9
                break
        #print(num)
        else:
            count += 1
            num = Next(num)
            #print("count = ", count)
            if len(num) == 1:
                count += 8
                break
    print(count)