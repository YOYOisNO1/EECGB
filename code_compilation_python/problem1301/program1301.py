def program1301():
    n = int(input())
    nabor = str(input())
    print(nabor.count("8"))
    if len(nabor) < 11:    
        print(0)
    elif(nabor.count("8") >= n // 11):
        print(n // 11)
    elif(0 < nabor.count("8") < n //11):
        print(nabor.count("8")
    else:
        print(0)