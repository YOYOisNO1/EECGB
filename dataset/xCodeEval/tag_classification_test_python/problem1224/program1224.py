def program1224():
    n=input()
    number=int(n)
    arr=[]
    i=2
    uno=1
    if(number==1):
        print(number)
    else: 
        arr.append(int(number))
        while number != 1 :
            while i<=number:
                if (number%i ==0):
                    number=number/i
                    arr.append(int(number))
                    break
                i=i+1
        #arr.append(int(number)) #imprime el 1 que falta 
    print(*arr)