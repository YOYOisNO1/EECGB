def program3847():
    import math
    a = list(input())
    letter = a.pop()
    num = int(''.join(a))
    h = {'a' : 4, 'b' : 5, 'c' : 6,
         'f' : 1, 'e' : 2, 'd' : 3}
    result = (math.ceil(num / 4) - 1) * 16 + [7, 0][((num % 4) & 1)] + h[letter]
    print(result)