def program1919():
    import re
    
    n = input()
    s = input()
    dict = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    
    for i in dict:
        result = re.match(s, i, 0)
        if result:
            print i
            break