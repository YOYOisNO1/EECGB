def program4794():
    n = int(input())
    home = input()
    
    t = [0, 0]
    
    for i in range(n):
        a = input().split('->')
        if a[0] == home:
            t[0] += 1
        elif a[1] == home:
            t[1] += 1
    
    if bool(abs(t[1] - t[0]) & 1):
        print('contest')
    else:
        print('home')