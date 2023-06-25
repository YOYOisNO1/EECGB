def program2425():
    import re
    
    n = input()
    text = input()
    
    #find inside parentheses
    tokens = re.findall('\(.*?\)',text)
    strip_tokens = [re.sub('[\(\)]','',x) for x in tokens]
    words = []
    for token in strip_tokens:
    	words.extend([x for x in token.split("_") if len(x) > 0])
    
    #find outside parentheses
    words_outside = re.compile('\(.*?\)|[\(\)\_]').split(text)
    words_length = [len(x) for x in words_outside if len(x) > 0]
    if len(words_length) > 0:
    	max_length = max(words_length)
    else:
    	max_length = 0
    
    print(max_length,len(words))