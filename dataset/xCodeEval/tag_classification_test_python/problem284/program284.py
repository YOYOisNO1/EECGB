def program284():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        if li[i] not in dic:
            dic[li[i]] = i
    
    if len(dic) < k:
        print("NO")
    else:
        print("YES")
        for i in list(dic.values())[:k]:
            print(i + 1, end=' ')