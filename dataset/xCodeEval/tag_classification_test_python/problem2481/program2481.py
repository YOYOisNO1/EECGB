    #!/usr/bin/python
    
    from collections import deque
    from collections import Counter
    
def ir():
        return int(input())
    
    n = ir()
    s = input()
    
def pw(i, j):
        global m, nw
        if b:
            nw += 1
        else:
            c = j - i
            if c > m: m = c
    
    i = 0; b = False; nw = 0; m = 0
    while True:
        if i == n: break
        # read spaces
        while i != n and s[i] == '_': i += 1
        # read word
        j = i
        while j != n and s[j] != '_' and s[j] != '(' and s[j] != ')': j += 1
        if i != j: pw(i, j); i = j
        if i == n: break
    
        # read '('
        if s[i] == '(': i += 1; b = True
        if s[i] == ')': i += 1; b = False
        
    print(m,) nw    