def program2427():
    # Online Python compiler (interpreter) to run Python online.
    # Write Python 3 code in this online editor and run it.
    charLength = int(input())
    string = input()
    
    out_dict = {
        'longest_length': 0,
        'n_par_words': 0,
        'word_length': 0, 
        'par': False
    }
    
    for i, char in enumerate(string):
        if char != '_' and char != '(' and char != ')':
            out_dict['word_length'] += 1
        else: 
            if out_dict['word_length'] > 0 and out_dict['word_length'] > out_dict['longest_length'] and not out_dict['par']:
                out_dict['longest_length'] = out_dict['word_length']
            elif out_dict['word_length'] > 0 and out_dict['par']:
                
                out_dict['n_par_words'] += 1
            out_dict['word_length'] = 0
        
        if char == '(':
            out_dict['par'] = True
        elif char == ')': 
            out_dict['par'] = False
        
    if out_dict['word_length'] > out_dict['longest_length']:
        out_dict['longest_length'] = out_dict['word_length']
    
    print(out_dict['longest_length'], out_dict['n_par_words'])