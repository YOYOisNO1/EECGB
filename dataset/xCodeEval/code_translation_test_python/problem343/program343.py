def program343():
    a = input()
    b = input()
    c = str(int(a)+int(b))
    ca = a.replace('0', '')
    cb = b.replace('0', '')
    cc = c.replace('0', '')
    more_c = str(int(ca)+ int(cb))
    if(more_c == cc):
        print("YES")
    else:
        print("NO")
    