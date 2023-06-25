    from sys import stdin, stdout
    n, l, r = map(int, stdin.readline().split())
    d = {}
    
    
def value(n):
        if n <= 1:
            return min(n, 1)
        else:
            return value(n // 2) * 2 + (n % 2)
        
    
def numerals(n):
        if n <= 1:
            return 1
        else:
            return numerals(n // 2) * 2 + 1
    
    
def cnt(l, r, left, right, number):
        m = left + (right - left) // 2
        ans = 0
        
        if l == left and r == right:
            if not number in d:
                d[number] = value(number)
                
            return d[number]
        
        
        if l < m:
            ans += cnt(l, min(m - 1, r), left, m - 1, number // 2)
        
        if r >= m >= l:
            ans += number % 2
        
        if r > m:
            ans += cnt(max(m + 1, l), r, m + 1, right, number // 2)
        
        return ans
    
    
    stdout.write(str(cnt(l, r, 1, numerals(n), n)))