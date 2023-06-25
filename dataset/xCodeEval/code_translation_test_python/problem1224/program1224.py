def program1224():
    d='dot'
    R=str.replace
    s=R(input(),d,'.')
    s=s[0]+R(s[1:],'at','@',1)
    if s[0]=='.':s=d+s[1:]
    if s[-1]=='.':s=s[:-1]+d
    print(s)