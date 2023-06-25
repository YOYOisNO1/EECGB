def program1626():
    import string
    m=[]
    s=str(input())
    for element in s:
        m.append(element)
    m.sort()
    print(m[-1]*s.count(m[-1]))