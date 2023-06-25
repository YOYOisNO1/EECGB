def program4664():
    n, k = map(int, input().split())
    entrances = input()
    di = {}
    s = set()
    for i in range(n): di[entrances[i]] = i
    
    for i in range(n):
        s.add(entrances[i])
        if len(s)>k:
            print("YES")
            break
        if di[entrances[i]]==i:
            s.remove(entrances[i])
    else:
        print("NO")