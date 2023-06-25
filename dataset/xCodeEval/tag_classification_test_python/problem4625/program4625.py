def program4625():
    from sys import stdin
    n, k = map(int, input().strip().split(" "))
    s = stdin.readline().rstrip()
    sum_hash = [0 for _ in range(26)]
    cur_hash = [0 for _ in range(26)]
    
    for c in s:
        sum_hash[ord(c) - ord('A')] += 1
    
    printyes = False
    guard_need = 0
    for c in s:
        if cur_hash[ord(c) - ord('A')] == 0:
            guard_need += 1
    
        if guard_need > k:
            printyes = True
    
        cur_hash[ord(c) - ord('A')] += 1
        if cur_hash[ord(c) - ord('A')] == sum_hash[ord(c) - ord('A')]:
            guard_need -= 1
    
    if printyes:
        print("YES")
    else:
        print("NO")