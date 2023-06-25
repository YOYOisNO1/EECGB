def program5533():
    s=input()
    n=int(s.replace('4','0').replace('7','1'), 2)
    print(n-1+2**len(s))