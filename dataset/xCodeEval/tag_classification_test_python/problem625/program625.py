def program625():
    import re
    input()
    print(max(map(lambda w: len(set(w)), re.split('[A-Z]', input()))))