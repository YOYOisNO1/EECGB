def program2468():
    n = int(input())
    s = input()
    strings1 = []
    strings2 = []
    string = ""
    f = False
    for letter in s:
        if letter == '_':
            if string and not f:
                strings1.append(string)
            if f and string:
                strings2.append(string)
            string = ""
        elif letter == '(':
            f = True
            if string:
                strings1.append(string)
            string = ""
        elif letter == ')':
            f = False
            if string:
                strings2.append(string)
            string = ""
        else:
            string += letter
    if string:
        strings1.append(string)
    try:
        print(len(max(strings1, key=len)), len(strings2))
    except BaseException:
        print(0, len(strings2))