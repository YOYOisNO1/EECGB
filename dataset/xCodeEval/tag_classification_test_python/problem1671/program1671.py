def program1671():
    '''
    Created on Jan 25, 2015
    
    @author: mohamed265
    '''
    num = input()
    ress = input()
    res = []
    for i in range(len(ress)):
        res.append(ress[i])
    num = sorted(num)
    #print(res,num)
    index = 0
    for i in range(len(num)):
        if num[i] != '0':
            index = i
            break
    if index == 0:
        print("OK") if num == res else print("WRONG_ANSWER")
    else:
        #print(num,index)
        temp = [num[index]] 
        for i in range(index):
            temp.append("0")
        for i in range(index+1,len(num)):
            temp .append( num[i])
        #print(temp)
        print("OK") if temp == res else print("WRONG_ANSWER")