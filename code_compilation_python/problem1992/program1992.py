def program1992():
        n = int(input())
        l = list(map(int, input().split()))
        
        s = sorted(list(set(l)))
        if len(s) < 3: return 'NO'
    
        '''count = 1
        flag = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if abs(s[i] - s[j]) <= 2 and i != j:
                    count += 1
                    if count >= 3: return 'YES'
            if count == 1:
                count += 1
            count -= 1'''
    
        for i in range(len(s)):
            for j in range(len(s)):
                for k in range(len(s)):
                    if max(s[i],s[j],s[k]) - s[i] + max(s[i],s[j],s[k]) - s[j] + max(s[i],s[j],s[k]) - s[k] == 3 and i != j and i != k and j != k:
                        return 'YES'
        
        return 'NO'
    
    print(main())