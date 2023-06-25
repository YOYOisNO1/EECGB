    
def get_pidor(s):
        govno = 0
    
        for c in s:
            if c.isupper():
                govno += 1
    
        return govno
    
    input()
    
    words = input().split(' ')
    
    max_hui = 0
    
    for w in words:
        hui = get_pidor(w)
    
        if hui > max_hui:
            max_hui = hui
    
    print(max_hui)
    