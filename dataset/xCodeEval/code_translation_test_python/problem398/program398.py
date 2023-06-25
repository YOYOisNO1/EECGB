    
def to_trenary(n):
        result = ''
        while n != 0:
            result += str(n % 3)
            n //= 3
        return ''.join(list(reversed(result)))
    
    
def from_trenary(n):
        result = 0
        c_base = 1
        n = reversed(n)
        for pos in n:
            result += c_base * int(pos)
            c_base *= 3
        return result
    
    
def compl(a, c):
        return str((int(c) - int(a) + 3) % 3)
    
    
    a, c = map(int, input().split())
    a_tr, c_tr = to_trenary(a), to_trenary(c)
    if len(a_tr) < len(c_tr):
        a_tr = '0' * (len(c_tr) - len(a_tr)) + a_tr
    else:
        c_tr = '0' * (len(a_tr) - len(c_tr)) + c_tr
    
    
    b_tr = [0 for _ in range(len(a_tr))]
    for i in range(len(b_tr)):
        b_tr[i] = compl(a_tr[i], c_tr[i])
    
    b_tr = ''.join(b_tr)
    b = from_trenary(b_tr)
    print(b)