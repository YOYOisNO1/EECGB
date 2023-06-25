    li=[i for i in range(1,11)]
    
def boringapartments(x):
        count = 0
        count += 10*(int(x[0])-1)
        # for i in range(1,int(x[0])):
        #     count+=10
        var = len(x)
        if var == 1:
            count+=1
        elif var == 2:
            count +=3
        elif var == 3:
            count +=6
        else:
            count+=10
        print(count)
    
    
    tc = int(input())
    for i in range(tc):
        x = input()
        boringapartments(x)