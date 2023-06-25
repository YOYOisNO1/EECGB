def program3735():
    inp = int(input())
    output = '';
    flag = False
    
    if(inp>36):
        print(-1);
        flag = True;
    
    if(inp == 0):
        print(1);
        flag = True;
    
    if(inp == 1):
        print(4);
        flag = True;
    
    if flag == False:
        while (inp != 0):
            if inp >= 2:
                output = output + '8'
                inp -= 2
            else:
                output = output + '0'
                inp -= 1
    
        print(output)