def solve(s):
        number = ""    i = 0
    
        while i < len(s):
            if s[i] == ".":
                number += "0"
            elif s[i] == "-":            
                if s[i+1] == ".":
                    number += "1"
                    i += 1
                elif s[i+1] == "-":
                    number += "2"
                    i += 1
            i += 1
        
        return number
    
    
    inp = list(input())
    print(solve(inp))