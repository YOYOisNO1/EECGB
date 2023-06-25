def program2453():
    n = input()
    string = input()
    
    outside_parens = '_'.join([x.split(')')[-1] for x in string.split('(')])
    words = sorted(outside_parens.split('_'), key=len)
    longestWord = len(words[-1])
    
    inside_parens = '_'.join([x.split(')')[0] for x in string.split('(')][1:])
    word_count = len([x for x in inside_parens.split('_') if x])
    
    print(longestWord, word_count)