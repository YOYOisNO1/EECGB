def program1675():
    n , m = map(int,input().split())
    count = 0
    for i in range(101):
        a = i
        aa = a * a
        b = n - aa
        if a + (b * b) == m and b >= 0:
            count += 1 
        
    print((count)) 