def program1045():
    a = input()
    b = int(input())
    lst = sorted(a)
    c = 0
    for i in range(len(lst)):
        for j in range(len(lst) - 1, i - 1, -1):
            x = lst[:i] + [lst[j]] + sorted(lst[i:j]) + lst[j + 1:]
            
            if int(''.join(x)) <= b and int(''.join(x)) > c:
                c = int(''.join(x))
                lst = x
    print(int(''.join(lst)))