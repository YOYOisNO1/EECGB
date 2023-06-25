def program415():
    s=input()
    s=s.replace("+",'')
    l=list(map(int,s))
    l.sort()
    p=''
    for i in l:
        p+=str(i)
        p+=("+")
    print(p[:-1])    
        