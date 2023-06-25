def go(a, b):
        s = a + b
        if a == 0 and b == 1:
            return "Yes"
    
        if s % 2 != 1:
            return "No"
        if (s + 1) / 2 < b:
            return "No"
        if a > s - 2:
            return "No"
    
        return "Yes"
    
    a, b = map(int, input().split())
    #print(a,) b
    print(go(a,) b)