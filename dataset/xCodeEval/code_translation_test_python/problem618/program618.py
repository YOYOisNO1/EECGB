def program618():
    s = input()
    x = s[::-1]
    if len(s) ==1:
        print('YES')
        exit()
    if s == x:
        if len(s)%2 ==1:
            print('YES')
        else:
            print('NO')
        exit()
    
    r = len(s)/2
    c =0
    for x in range(r):
        if s[x] !=s[len(s)-1-x]:
            c= c+1
    
    if c ==1:
        print('YES')
    else:
        print('NO')