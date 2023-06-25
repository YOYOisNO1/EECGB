def program2431():
    n = input()
    s = str(input())
    maxWordLengthOutOfBrackets = 0
    numberWordInBrackets = 0
    inBrackets = False
    currentWidth = 0;
    for i in range(len(s)):
        if(s[i] == '('):
            inBrackets = True;
            currentWidth = 0;
            if(s[i+1] != '_' and s[i+1]!= ')'):
                numberWordInBrackets +=1;
        elif(s[i] == ')'):
            inBrackets = False;
            currentWidth = 0;
        elif(s[i] == '_'):
            currentWidth = 0;
            if(inBrackets and s[i+1] != '_' and s[i+1] != ')'):
                numberWordInBrackets +=1;
        else:
            currentWidth +=1
            if(inBrackets == False and currentWidth > maxWordLengthOutOfBrackets):
                maxWordLengthOutOfBrackets = currentWidth
    print(maxWordLengthOutOfBrackets, numberWordInBrackets)
        
            