def program1907():
    n=input()
    s=[int(i) for i in range(ord('a'),ord('z')+1)]
    s=s[::-1]
    for i in n:
        a=ord(i)
        if a==s[-1]:
            s.pop()
        elif a>s[-1]:
            print('NO')
            exit()
    print('YES')