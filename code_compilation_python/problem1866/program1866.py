def program1866():
    number,k = input().split(' ')
    
    if(len(number)<=int(k)):
        print(len(number)-1)
    else:
        countZero = 0
        countDelete = 0
        for i in range(1,len(number)+1):
            if(countZero==int(k)):
                break
            if(number[-i]=='0'):
                countZero+=1
            else:
                countDelete+=1
        if(len(number)-(countDelete)<int(k)+1)
        print(countDelete)