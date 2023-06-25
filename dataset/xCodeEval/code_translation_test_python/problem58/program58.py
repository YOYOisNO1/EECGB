    #!/usr/bin/python
def triangle(l):
        return l[0] + l[1] > l[2]
    
def degenerate(l):
        return l[0] + l[1] == l[2]
    
def solve(l):
        for i in range(4):
            copy = list(l)
            del copy[i]
            if triangle(copy):
                return "TRIANGLE"
    
        for i in range(4):
            copy = list(l)
            del copy[i]
            if degenerate(copy):
                return "SEGMENT"
        return "IMPOSSIBLE"
    
    l = sorted(map(int, input().split(" ")))
    
    print(solve(l))