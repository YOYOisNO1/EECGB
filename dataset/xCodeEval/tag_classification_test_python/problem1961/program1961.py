def program1961():
    n = input()
    
    n = n.replace('>', '1000')
    n = n.replace('<', '1001')
    n = n.replace('+', '1010')
    n = n.replace('-', '1011')
    n = n.replace('.', '1100')
    n = n.replace(',', '1101')
    n = n.replace('[', '1110')
    n = n.replace(']', '1111')
    print(int(n, 2)%1000003)