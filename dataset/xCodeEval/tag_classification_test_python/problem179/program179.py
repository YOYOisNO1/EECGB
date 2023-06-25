def firstDP(mainString, string, i, n):
    
        if i == len(mainString):
            if string == "QAQ":
                return 1
            else:
                return 0
    
        if n == 3:
            if string == "QAQ":
    
                return 1
            else:
                return 0
    
        noOfSubsequences = firstDP(mainString, string + mainString[i], i + 1, n + 1) + firstDP(mainString, string, i + 1, n)
    
        return noOfSubsequences
    
    
    s = input()
    print(firstDP(s, "", 0, 0))