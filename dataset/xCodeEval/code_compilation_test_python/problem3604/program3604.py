def check(temp,a):
        dr = {}
        nums = '0123456789'
        a = list(str(a));
        for i in range(len(temp)):
            if temp[i] == '?':
                if a[i] in nums:
                    continue
                else:
                    return 0
            if temp[i] in nums:
                if temp[i] == a[i]:
                    continue
                else:
                    return 0
            if temp[i] != '?':
                if temp[i] not in nums:
                    if temp[i] not in dr.keys() and a[i] not in dr.values():
                        dr[temp[i]] = a[i]
        for i in range(len(temp)):
            if temp[i] != '?' and temp[i] not in nums and a[i]:
                
                if temp[i] not in dr.keys() or a[i] != dr[temp[i]]:
                    return 0
        return 1
            
    n = input()
    leng = len(n)
    ans = 0
    for i in range(10**(leng-1),10**leng):
        if check(n,i) == 1:
            ans += 1
    print(ans)