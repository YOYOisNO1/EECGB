def program902():
    a = int(input())
    
    sum = 0
    count = 0
    for i in range(1,10001):
        sum_temp = 0
        for m in range(1,i+1):
            sum_temp+=m
        sum+= sum_temp
        if sum <= a:
            count+=1
        else:
            break
    print(count)