    s = input()
    
def divisibility(s):
    
        n = len(s)
    
        for i in range(n):
    
            for j in range(-1, i):
    
                for k in range(-1, max(0, j)):
    
                    val = 0
    
                    val += int(s[i])
    
                    if j != -1:
                        
                        val += 10*int(s[j])
                    
                    if k != -1:
    
                        val += 100*int(s[k])
    
                    if not val%8:
    
                        print("YES")
    
                        print(val)
    
                        return 0
    
        return 1
    
    if (divisibility(s)):
    
        print("NO")