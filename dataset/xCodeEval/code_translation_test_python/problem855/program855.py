def program855():
    l = list(str(input()))
    result = 0
    for x in l:
        if x in 'aeiou13579':
            result += 1
    print(result)