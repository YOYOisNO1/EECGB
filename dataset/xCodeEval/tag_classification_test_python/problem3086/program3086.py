def program3086():
    
    N = int(input().strip())
    L = list(input().strip())
    
    i = 0
    while i<len(L)-1:
        if L[i] == 'R' and L[i + 1] == 'U' or \
           L[i] == 'U' and L[i + 1] == 'R':
            if i+2 < len(L):
                L = L[:i]+['D']+L[i+2:]
            else:
                L = L[:i] + ['D']
        i += 1
    print(len(L))