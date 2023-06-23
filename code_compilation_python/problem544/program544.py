def program544():
    input_list = []
    for i in range (5):
        value = input ()
        input_list.append(value)
    
    total = int(input_list[4])
    num1 = int(input_list[0])
    num2 = int(input_list[1])
    num3 = int(input_list[2])
    num4 = int(input_list[3])
    main_list = []
    
    for i in range (1, ((total // num1)+1)):
        main_list.append(i*num1)
    for i in range (1, (total // num2)+1):
        main_list.append(i*num2)
    for i in range (1, (total // num3)+1):
        main_list.append(i*num3)
    for i in range (1, (total // num4)+1):
        main_list.append(i*num4)
        
    main_list.sort()
    list2 = []
    for i in main_list: 
        if i not in list2: 
            list2.append(i) 
    print list2
    print (len(list2))
        
            
            
            
            