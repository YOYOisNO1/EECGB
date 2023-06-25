    #!/usr/bin/python
    
def ir(): return int(input())
def ia(): return map(int, input().split())
    
    n = ir()
    a = ia()
    
    m = max(a)
    
    print("EASY") if m == 0 else "HARD"