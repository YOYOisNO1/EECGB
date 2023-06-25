def program2455():
    import sys
    
    num, content = sys.stdin.readlines()
    
    max_len = 0
    started = False
    words_inside = 0
    inside = False
    current_len = 0
    for i, c in enumerate(content.strip()):
        if c == '_':
            if started:
                if inside:
                    words_inside += 1 
                else:
                    max_len = max(max_len, current_len)
            current_len = 0
            started = False
        elif c == '(': 
            if started:
                max_len = max(max_len, current_len)
            current_len = 0
            inside = True
            started = False
        elif c == ')':
            if started:
                words_inside += 1
            current_len = 0
            inside = False
            started = False
        else:
            started = True
            current_len += 1
    if started:
        max_len = max(max_len, current_len)
    
    print(str(max_len)) + ' ' + str(words_inside)