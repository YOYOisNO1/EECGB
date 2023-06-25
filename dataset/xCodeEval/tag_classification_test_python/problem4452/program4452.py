def program4452():
    str=input()
    newStr=str[0]+str[1:].replace('at','@',1)
    str=newStr[0]+newStr[1:-1].replace('dot','.')+newStr[-1]
    
    
    print(str)
    
    
    