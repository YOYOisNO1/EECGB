    n = int(input())
    s = input()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = 100000000
    
    
def diff(c1, c2):
        if letters.find(c1) > letters.find(c2):
            c1, c2 = c2, c1
        return min(abs(letters.find(c1) - letters.find(c2)), 26-abs(letters.find(c1) - letters.find(c2)))
    
    
    for i in range(n-3):
        count = 0
        count = diff('A', s[i]) + diff('C', s[i+1]) + \
            diff('T', s[i+2]) + diff('G', s[i+3])
        ans = min(ans, count)
    
    print(ans)