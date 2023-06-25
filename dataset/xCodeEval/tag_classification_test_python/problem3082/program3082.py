def program3082():
    n = int(input())
    m = input()
    
    
    d = ['UR', 'RU']
    tamanho = n
    
    i = 0
    while i < len(m)-1:
        if m[i] + m[i + 1] in d:
            tamanho -= 1
            i += 2
        else:
            i += 1
    
    print(tamanho)