def program249():
    word = str(input())
    upperCase = 0
    lowerCase  = 0
    for element in word:
        if element >= 'a' and element <= 'z':
            lowerCase+=1
        elif(element >= 'A' and element <='Z'):
            upperCase+=1
    
    if lowerCase >= upperCase:
        print(word.lower())
    else :
        print(word.upper())
    