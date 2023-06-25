def program379():
    n=input()
    l=len(n)//2
    p=n.count("a")
    if p>l:
        print(len(n))
    else:
        print(2*p-1)