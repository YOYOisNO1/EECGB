    # ABBYY Cup 3.0
    # Problem A: Special Task
    
def codes(s):
        number = 1
        letters = []
        for i in xrange(len(s)):
            if (s[i] == "?"):
                if (i == 0):
                    number *= 9
                else:
                    number *= 10
            elif (s[i].isalpha() and (s[i] not in letters)):
                letters += [s[i]]
        if (s[0].isalpha()):
            number *= 9
            for j in xrange(len(letters)-1):
                number *= 9-j
        else:
            for j in xrange(len(letters)):
                number *= 10-j
        return number
    
    s = input("")
    print(codes(s))