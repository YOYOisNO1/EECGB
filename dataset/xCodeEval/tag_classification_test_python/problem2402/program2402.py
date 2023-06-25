def program2402():
    n = int(input())
    s = input()
    brk_start = False
    word_len,word_cnt,word_max_len=0,0,0
    for i in s:
        if i == "(":
            word_max_len = max(word_max_len,word_len)
            brk_start = True
            word_len = 0
        elif i == ")":
            if word_len > 0: word_cnt +=1
            brk_start = False
            word_len = 0
        elif i == "_":
            if word_len > 0:
                if brk_start:
                    word_cnt +=1
                else:
                    word_max_len = max(word_max_len,word_len)
                word_len = 0
        else:
            word_len+=1
    else:
        word_max_len = max(word_max_len,word_len)
    
    print(word_max_len,word_cnt)