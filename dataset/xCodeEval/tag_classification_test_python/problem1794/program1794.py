def program1794():
    n = int(input())
    m = input()
    m = m.split()
    for i in range(len(m)):
        m[ i ] = int(m[ i ])
    m.sort()
    
    for i in m:
        print(i)