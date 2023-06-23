def program1633():
    text = input()
    bracket = False
    bracket_word_count = 0
    max_length = 0
    bracket_s = ""
    not_bracket_s = ""
    for ch in text:
    	if bracket:
    		if ch == ')':
    			bracket = False
    			bracket_word_count += sum(1 for s in bracket_s.split('_') if s)
    			bracket_s = ""
    		else:
    			bracket_s += ch
    	else:
    		if ch == '(':
    			bracket = True
    			max_length = max(max_length, max(len(s) for s in non_bracket_s.split('_'))
    			non_bracket_s = ""
    		else:
    			non_bracket_s += ch
    max_length = max(max_length, *(len(s) for s in non_bracket_s.split('_'))
    bracket_word_count += sum(1 for s in bracket_s.split('_') if s)
    print('{} {}'.format(max_length, bracket_word_count))