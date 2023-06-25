def program1252():
    input(); count = 0
    for c in input():
        if c=='+':count+=1
        else:
            if count: count-=1
    print(count)