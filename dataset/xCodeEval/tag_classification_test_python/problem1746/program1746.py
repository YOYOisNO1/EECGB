def program1746():
    s1=input()
    s2=input()
    n=''
    m=''
    for char in s1:
        m+=char.lower()
    for char in s2:
        n+=char.lower()
    if m == n:
        print(('0'))
    elif m > n :
        print(('1'))
    else:
        print(('-1'))