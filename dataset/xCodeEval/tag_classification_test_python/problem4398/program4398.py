def program4398():
    s = input()
    email = s[0]
    pointer = 1
    at_not_used = True
    while pointer < len(s):
        if s[pointer] == 'd' and pointer < len(s) - 3 and s[pointer:pointer + 3] == 'dot':
            email += '.'
            pointer += 3
        elif s[pointer] == 'a' and pointer < len(s) - 1 and s[pointer:pointer + 2] == 'at' and at_not_used:
            email += '@'
            at_not_used = False
            pointer += 2
        else:
            email += s[pointer]
            pointer += 1
    print(email)