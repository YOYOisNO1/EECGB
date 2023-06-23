def program3599():
    //f = open('Text.txt',"r")
    n = int(f.read())
    res = 0
    
    for x in range(3, n+1):
        res += 1*(x-1)*(x)
    
    print(res)