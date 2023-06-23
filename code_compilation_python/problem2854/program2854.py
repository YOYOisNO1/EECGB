def program2854():
    a, ta = map(int, input().split())
    b, tb = map(int, input().split())
    s = list(input())
    
    p = s.index(':')
    time = int(''.join(s[:p])) * 60 + int(''.join(s[p+1:]))
    
    s = 0
    
    if time >= 601 :
        s += 1
    if time + ta <= 1439 :
        s += 1
    
    s += ((ta - b) - (-tb + b))//b
    print s