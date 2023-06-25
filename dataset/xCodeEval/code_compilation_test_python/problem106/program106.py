def program106():
    numbers=[int(x) for x in input().split()]
    
    if numbers[0]==1 and numbers[1]==1:
        print(-1)
    elif numbers[0]==1 and numbers[1]==3:
        print(-1)
    else:
        for i in range(numbers[0], numbers[1]+1):
            
            if i%2!=0:
                continue
            else:
                if abs(numbers[0]-numbers[1]) < 2:
                    print("-1")
                else:
                    print(i,i+1, i+2)
                break