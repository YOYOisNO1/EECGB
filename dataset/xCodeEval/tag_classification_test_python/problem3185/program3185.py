def program3185():
    a = input()
    count = 0
    countd = 0
    b = a[0]
    
    
    for i in a[1:]:
        if b != i:
            countd = 0
            count = count+1
        if b == i:
            countd = countd +1
        if countd == 5:
            count = count +1
            countd = 0
    
        b = i
    
    
    print(count+1)