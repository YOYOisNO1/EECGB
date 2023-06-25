def program919():
    from collections import Counter
    l = []
    n = int(input())
    s = input()
    
    for i in range(n - 1):
        l.append(s[i] + s[i + 1])
        
    mx , nm = Counter(l).most_common(1)[0]
    
    print(mx)
        