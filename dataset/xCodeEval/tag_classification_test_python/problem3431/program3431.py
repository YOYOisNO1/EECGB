def program3431():
    s = input()
    n = len(s)
    t = (n-1)//2
    if '1' in s[1:] or n%2==0:
        t += 1
    print(t)
    