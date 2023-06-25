def program2441():
    input()
    text = input()
    
    longest_out = 0
    current_count = 0
    in_paren = False
    words_in_paren = 0
    paren_count = 0
    
    for c in text:
        if current_count > longest_out:
            longest_out = current_count
        if c == '(':
            in_paren = True
            current_count = 0
            paren_count = 0
            continue
        if c == ')':
            if paren_count > 0:
                words_in_paren += 1
            in_paren = False
            continue
        if c == '_':
            if paren_count > 0 and in_paren:
                words_in_paren += 1
            current_count = 0
            paren_count = 0
            continue
        if not in_paren:
            current_count += 1
            paren_count = 0
        else:
            paren_count += 1
    if current_count > longest_out:
        longest_out = current_count
    
    print("%s %s") % (longest_out, words_in_paren)