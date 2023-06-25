def program2415():
    n = input()
    stri = input()
    
    tmp_letters = 0
    inbracket = False
    maxlen = 0
    word_count = 0
    haswords = True
    for word in str(stri):
        if word == '(':
            if tmp_letters > maxlen:
                maxlen = tmp_letters
            tmp_letters = 0
            inbracket = True
            haswords = False
        if inbracket:
            if word.isalpha() or word.isalpha():
                haswords = True
            if (word == '_' or word == ')') and haswords:
                word_count += 1
                haswords = False
            if word == ')':
                inbracket = False
        else:
            if word.isdigit() or word.isalpha():
                haswords = True
                tmp_letters += 1
            if word == '_' and haswords:
                if tmp_letters > maxlen:
                    maxlen = tmp_letters
                    haswords = False
                tmp_letters = 0
    if tmp_letters > maxlen:
        maxlen = tmp_letters
        haswords = False
    tmp_letters = 0
    print(maxlen,) word_count