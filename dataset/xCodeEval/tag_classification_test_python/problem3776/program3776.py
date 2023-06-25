def program3776():
    num1 = int(input())
    num2 = input()
    binary1 = format(num1, 'b')
    temp = list(num2)
    #binary2 = int(''.join(map(str,binary2)),base=2)
    if(num1==1):
        print(''.join(temp))
    else:
        while(temp.count('1')>1):
            temp.remove('1')
        s = '1'
        for _ in range(len(temp)-1):
            s += '0'
        print(s)
        