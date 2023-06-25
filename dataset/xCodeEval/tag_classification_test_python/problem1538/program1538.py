def program1538():
    s = input()
    instruction = input()
    i = 0
    pos = 0
    for char in instruction:
        if char == s[pos]:
            pos = pos + 1
    print(pos) + 1