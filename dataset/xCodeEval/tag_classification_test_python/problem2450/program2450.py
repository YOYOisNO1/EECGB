def program2450():
    n = int(input())
    s = input()
    max_word = 0
    word_len = 0
    in_br = 0
    bracket = False
    last = ''
    
    for i in range(n):
        if s[i] == '_' and last.isalpha():
            if not bracket and max_word < word_len:
                max_word = word_len
            word_len = 0
            if bracket:
                in_br += 1
        elif s[i] == '(':
            if max_word < word_len:
                max_word = word_len
            word_len = 0   
            bracket = True
        elif s[i] == ')':
            bracket = False
            if last.isalpha():
                in_br += 1
            word_len = 0        
        elif s[i].isalpha():
            word_len += 1
            if not bracket and max_word < word_len:
                max_word = word_len
            #print(s[i], word_len, max_word)
        last = s[i]
            
    print(max_word, in_br)           