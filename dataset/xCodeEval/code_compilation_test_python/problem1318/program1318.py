def program1318():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    s = input().split()
    for i in range(a[0]):
        s[i] = int(s[i])
    b = input().split()
    for i in range(a[1]):
        b[i] = int(b[i])
    max = a[2]
    for i in s:
         for j in b:
            if int(a[2]/i)*j > max:
                max = int(a[2]/i)*j + a[2] - int(a[2]/i)*i
    print(max)