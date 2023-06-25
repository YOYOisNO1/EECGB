    import sys
    input = sys.stdin.readline
    
def main():
        n = int(input())
        s = "&" + input()
        s += "&"
        ans = 0
        for i in range(97  + 26 - 1, 96, -1):
            j = 0
            while j < len(s) - 1:
                if ord(s[j]) == i:
                    if ord(s[j - 1]) + 1 == ord(s[j]) or ord(s[j + 1]) + 1 == ord(s[j]):
                        s = s[:j] + s[j + 1:]
                        ans += 1
                    else:
                        j += 1
                else:
                    j += 1
            j = len(s) - 1
            while j > 0:
                if ord(s[j]) == i:
                    if ord(s[j - 1]) + 1 == ord(s[j]) or ord(s[j + 1]) + 1 == ord(s[j]):
                        s = s[:j] + s[j + 1:]
                        ans += 1
                    else:
                        j -= 1
                else:
                    j -= 1            
                
                    
                    
                        
        print(ans)
                    
                    
    main()