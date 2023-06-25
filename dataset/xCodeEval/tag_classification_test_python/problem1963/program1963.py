def program1963():
    s = list(input())
    a =''
    
    for i in s:
        if i == ">":
            a += '1000'
        if i == "<":
            a += '1001'
        if i == "+":
            a += '1010'
        if i == "-":
            a += '1011'
        if i == ".":
            a += '1100'
        if i == ",":
            a += '1101'
        if i == "[":
            a += '1110'
        if i == "]":
            a += '1111'
    
    print(int(a,2)%1000003  )