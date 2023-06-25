def program2438():
    import sys
    
    n = sys.stdin.readline()
    line = sys.stdin.readline()
    
    words_out = line.strip().split('(')
    words1 = filter(lambda w: ')' not in w, words_out)
    words2 = filter(lambda w: ')' in w, words_out)
    words_in = map(lambda x: x.split(')')[0], words2)
    res2 = 0
    for word in words_in:
        res2 += len(filter(lambda x: x != '', word.split('_')))
    
    
    words2 = map(lambda x: x.split(')')[1], words2)
    words_out = words1 + words2
    res1 = 0
    for word in words_out:
        res1 = max(res1, max(map(len, word.split('_'))))
    
    print(res1,) res2