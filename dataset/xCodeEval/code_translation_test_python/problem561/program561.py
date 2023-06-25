def program561():
    n=input()
    if len(n)==1:
        print(0)
    elif n[::-1]!=n:
        print(len(n))
    else:
        while True:
            n=n[:-1]
            s=n[::-1]
            if s!=n:
                print(len(s))
                break
            elif len(s)==1:
                print(0)
                break
            