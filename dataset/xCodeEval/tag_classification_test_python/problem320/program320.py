def program320():
    n=int(input())
    s=input()
    while 'xxx' in s:
        s=s.replace('xxx','xx',1)
    print(n-len(s))