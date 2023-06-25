def program2884():
    import re
    pockemon = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    n = input()
    test = input()
    
    for i in pockemon:
        if re.match(test, i) and len(test) == len(i):
            print(i)