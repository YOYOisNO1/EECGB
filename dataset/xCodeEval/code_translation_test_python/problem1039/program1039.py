def program1039():
    from itertools import product
    
    s1 = sum([1 if i == '+' else -1 for i in input()])
    s2 = input()
    q = s2.count('?')
    x = []
    if q:
        s2 = s2.replace('?', '')
        for j in set(product('-+', repeat=q)):
            j = ''.join(j)
            x.append(sum([1 if i == '+' else -1 for i in j + s2]))
        a = len(x)
        print(float(len(filter(lambda) y: y == s1, x))) / float(a)
    else:
        x = sum([1 if i == '+' else -1 for i in s2])
        if x == s1:
            print(1)
        else:
            print(0)