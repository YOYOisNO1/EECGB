def program3627():
    n,t = map(int , input().split(' '))
    s = input()
    
    a = s.count('B')
    for i in range(t):
        s = s.replace('BG','GB',a)
    print(s)