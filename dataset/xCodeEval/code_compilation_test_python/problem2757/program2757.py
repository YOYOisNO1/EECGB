def program2757():
    n=input()
    t=int(input())
    b=[]
    c=0
    d=""
    for i in range(t):
        x=(input())
        b.append(x)
        d=d+x
    if len(b)>1:
        if d.count(n[0])>=n.count([n[0]) and d.count(n[1])>=n.count(n[1]):
            if any(c for c in b if c[1]==n[0] or c[0]==n[1]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if b[0]==n or b[0][::-1]==n:
            print("YES")
        else:
            print("NO")