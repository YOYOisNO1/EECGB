    a, b, c = map(int, input().split())
    
def s(x):
        return sum([int(i) for i in str(x)])
    sol = []
    for i in range(1, 82):
        x = b*i**a+c
        if s(x) == i:
            sol.append(x)
    
    sol = [x in sol if x > 0 and x < 10**9]
    ans = ""
    for x in sol:
        ans += str(x) + " "
    print len(sol)
    print ans.strip()