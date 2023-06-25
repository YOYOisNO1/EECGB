def program4586():
    n, k = map(int, input().split())
    entrances = input()
    d = {}
    s = set()
    for i in range(n): d[entrances[i]] = i
    
    for i in range(n):
        s.add(entrances[i])
        if len(s)>k:
            print("YES")
            break
        if d[entrances[i]]==i:
            s.remove(entrances[i])
    else:
        print("NO")