def program7006():
    s=input()
    f=False
    for i in range(1,len(s)):
        if s[i:]==s[:len(s[i:])] and len(s[i:])-1>=i:
            print('YES')
            print(s[i:])
            f=True
            break
    if not f:
         print('NO')