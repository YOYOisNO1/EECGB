def program1485():
    input_data = input().strip()
    input_data = input_data.lower()
    skeepme = 'aeiouy'
    output = ''
    for each in input_data:
        if each in skeepme:
            continue
        output += '.'
        output += each
    print(output)