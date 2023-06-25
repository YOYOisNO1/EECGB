def program3406():
    n = input()
    l1 = map(int, input().split())
    l2 = []
    for i in range(1, n-1):
        s = l1.pop(i)
        l2.append(sorted(l1))
        l1 =  [s] + l1
    l4 = []
    for i in l2:
        l3 = []
        for j in range(1, len(i)):
            l3.append(i[j]-i[j-1])
        l4.append(max(l3))
    print(min(l4))