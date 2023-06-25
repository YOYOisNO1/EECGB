def program343():
    s = input()
    n = len(s)
    ans = ''
    half = n//2
    
    evens = s[half+1:]
    odds = s[:half+1]
    
    for i in range(half):
        ans = ans + odds[half - i]
        ans = ans + evens[i]
    
    if n %2 == 1:
        ans = ans + odds[0]
        
    print(ans)