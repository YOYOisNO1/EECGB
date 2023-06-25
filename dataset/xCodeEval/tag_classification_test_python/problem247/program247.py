def program247():
    s=input()
    s=list(s)
    c=0
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            c=c+1 
    s=''.join(s)
    if c>len(s)/2:
        s=s.upper()
    else:
        s=s.lower()
    print(s)