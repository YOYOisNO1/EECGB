def DecimalToBinary(num): 
          
        if num > 1: 
            DecimalToBinary(num // 2) 
        a=num % 2
    num=(int)input()
    DecimalToBinary(num)
    print(a.count'1')