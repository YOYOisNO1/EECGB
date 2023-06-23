def program935():
    n = input()
    s = input()
    d = map(int, s.split())
    res = 0
    for a in d:
        res = res or d
    
    return 'easy' if res == 0 else 'hard'