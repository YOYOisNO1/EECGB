def program178():
    n=input()
    out=""
    for i in n:
        if i=='7':
            out+="1"
        else:
            out+="0"
    out=out[::-1]
    p=0
    for i in range(len(out)):
        if out[i]=='0':
            p+=2**i
        else:
            p+=2**(i+1)
    print(p)