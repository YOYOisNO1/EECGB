    # Date:2011-12-3
    # Author:Chika
    
    import re
    
    match_plus = re.compile('(^HQ9)\+')
    
def match_repl(matchobj):
        matchstr = matchobj.group(0)
        return chr(ord(matchobj.group(1)) + 1)
    
    p = input()
    
    while match_plus.search(p) is not None:
        p = match_plus.sub(match_repl, p)
        
    result = 'YES' if set(p) & {'H', 'Q', '9'} else 'NO'
    
    print(result)