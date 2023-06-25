def solve(a, b):
        return min((26 + a - b) % 26, (26 + b - a) % 26)
    
    
def main():
        n = int(input())
        s = input().lower()
        print(min((sum((solve(ord(a), ord(b)) for a, b in zip(s[i:i + 4], 'actg'))) for i in range(n - 3))))
    
    
    main()