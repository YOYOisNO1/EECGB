def program99():
    a = list(input().lower())
    b=str()
    for i in range(len(a)):
        if a[i] not in 'aoyeui':
            b += '.'+a[i]
    print(b)