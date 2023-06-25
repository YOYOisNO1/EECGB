def program441():
    line = str(input()).split()
    a = int(line[0])
    b = int(line[1])
    time = 0
    onFirst = False 
    if(a<b):
        onFirst = True
    do = True
    if(a==1 and b==1):
        print(0)
        do = False
    
    
    
    
    while(a > 0 and b > 0 and do = True):
        time = time+1
        if(a==1):
            onFirst = True
        if(b==1):
            onFirst = False
        if(a != 1 and b ==2):
            onFirst = False
        if(b != 1 and a ==2):
            onFirst = True
            
        if(onFirst == True):
            a = a+1
            b = b-2
        else:
            a = a-2
            b = b +1
    if(do = True):
        print(str(time))