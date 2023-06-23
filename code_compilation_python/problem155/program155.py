def program155():
    read = input()
    list1 = list(read)
    count = 0
    for i in range(len(list1)) :
        while list1[i]==list1[i-1] :
            count+=1
            if count== 7 :
                print("YES")
                print(i)
                break
    
    
    if count < 7 :
        print("NO")