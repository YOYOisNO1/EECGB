def solve(g, su, s, n):
        c = 0
        g2 = 0
        for i in range(n):
            c += int(s[i])
            
            if (c == su):
                c = 0
                g2 += 1        
            elif (c > su):
                return False
        if (c == 0 and g2 == g):
            return True    
    
def main():
        n = int(input())
        s = input()
        
        summ = 0
        
        for elem in s:
            summ += int(elem)
        
        g = 2
        i = 2
        
        ans = False
        
        while (g <= n):
            if (summ % g == 0):
                i = summ // g
                
                ans = solve(g, i, s, n)
                if (ans):
                    break
            g += 1
        
        if (ans):
            print("YES")
        else:
            print("NO")
        
    if __name__ == "__main__":
        main()