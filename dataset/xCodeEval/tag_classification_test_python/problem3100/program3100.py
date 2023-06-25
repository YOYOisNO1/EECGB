def program3100():
    count, answer, prev = 1,0,''
    for letter in input():
        if prev == letter:
            count += 1
        elif count & 1 == 0:
            answer += 1
            count = 1
        prev = letter
    if count & 1 == 0:
        answer += 1
    print(answer)