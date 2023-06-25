def program134():
    # cook your dish here
    n=int(input())
    out=""
    if n>38:
        print(-1)
    else:
        for i in range(n//2):
            out+="8"
        for i in range(n%2):
            out+="9"
        print(out)
        