def program66():
    s = input()
    curr = 0
    max_jump = 0
    for c in s:
        curr += 1
        max_jump = max(curr, max_jump)
        if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' or c == 'Y':
            curr = 0
    
    curr += 1
    max_jump = max(curr, max_jump)
    print(max_jump)