    #!/usr/bin/python
    
def ir():
        return int(input())
    
def ia():
        line = input()
        line = line.split()
        return map(int, line)
    
def solve():
        n, tm = ia()
        a = ia()
    
        s = sum(a)
        j = (n - 1)*10
    
        if s + j>tm:
            print(-1)
            return
    
        rem = tm - (s + j)
        ej  = rem / 5
    
        print(2*(n) - 1) + ej
        
    solve()