def program2456():
    #!/usr/bin/python
    
    import sys
    
    long_word = 0
    word_in_parent = 0
    
    line_length = sys.stdin.readline()
    line = sys.stdin.readline()
    
    flags = {'in_parent':0, 'word_len':0}
    
    for char in line:
        if char == '_' or char == '(' or char == ')' or char == "\n":
            if flags['in_parent'] == 0 and flags['word_len'] > long_word:
                long_word = flags['word_len']
            if flags['in_parent'] > 0 and flags['word_len'] > 0:
                word_in_parent += 1
            if char == '(':
                flags['in_parent'] += 1
            if char == ')':
                flags['in_parent'] -= 1
            flags['word_len'] = 0
        if char.isalpha():
            flags['word_len'] += 1 
    print("{} {}".format(long_word, word_in_parent))