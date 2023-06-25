def program2743():
    s = list(input())
    t = list(input())
    t.reverse()
    count = 0
    
    if len(s) != len(t):
        
        print("NO")
        
    else:
        
        for i in range(len(s)):
            if s[i] == t[i]:
                count += 1
        if count == len(s):
            print("YES")
        else:
            print("NO")