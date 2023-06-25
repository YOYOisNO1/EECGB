def strp(string):
        sets = []
        s = set()
        for c in string:
            if c.isupper():
                if len(s):
                    sets.append(s)
                s = set()
            else:
                s.add(c)
        if len(s):
            sets.append(s)
        
        return len(sets) and max(map(len,sets))
    
    
    input()
    string = input()
    print(strp(string))