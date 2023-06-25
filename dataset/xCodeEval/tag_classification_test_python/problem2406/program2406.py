def program2406():
    n = input()
    string = input()
    n = len(string)
    longest_len = 0
    word_inside = 0
    curWord = []
    inParen = False
    for i in range(n):
        if (string[i] == "_"):
            if (inParen):
                if (len(curWord) > 0):
                    word_inside += 1
            else:
                if (len(curWord) > longest_len):
                    longest_len = len(curWord)
            curWord = []
        elif (string[i] == "("):
            inParen = True
            if (len(curWord) > longest_len):
                longest_len = len(curWord)
            curWord = []
        elif (string[i] == ")"):
            inParen = False
            if (len(curWord) > 0):
                word_inside += 1
            curWord = []
        else:
            curWord.append(string[i])
    
    if (len(curWord) > longest_len):
        longest_len = len(curWord)
    
    print(str(longest_len) + " " + str(word_inside))
            