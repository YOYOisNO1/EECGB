def program495():
    from sys import stdin,stdout
    n=stdin.readline()
    m=n
    for i in range(len(n)):
        if n[i]!='1':
            m=m[1:]
        if n[i]=='1':
            break
    zero=m.count('0')
    if zero<6:
        stdout.write('no')
    else:
        stdout.write('yes')