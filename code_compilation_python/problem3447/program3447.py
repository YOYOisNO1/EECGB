def program3447():
    num = int(input())
    d = {}
    a = []
    for _ in range(num):
        card = int(input())
        if card not in d:
            d[card] = 1
            a.append(card)
        else:
            d[card] = d[card]+1
            
    if len(d) == 2 and d[a[0]]=d[a[1]]:
        print("YES")
        print(a[0],a[1])
    else:
        print("NO")
    
        