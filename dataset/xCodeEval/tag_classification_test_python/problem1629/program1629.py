def program1629():
    a=input()
    m=""
    ma=max(a)
    for  i in range(len(a)):
        if a[i]==ma:
            m+=a[i]
    print(m)