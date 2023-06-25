def program5531():
    l, m = input().split()
    
    string = input()
    
    
    
    string = string.split()
    
    flag = True
    
    temp = None
    for index, s in enumerate(string):
        if int(m) < int(s):
            temp = string[index:]
            break
        
        if index+1 == len(string):
            flag = False
            print(l)
    
    if temp != None:
        temp = list(reversed(temp))
        temp2 = list
        
        for index, s in enumerate(temp):
            
            if int(m) < int(s):
                temp2 = temp[index:]
                break
        
        if flag == True:
            print(int(l)-len(temp2))