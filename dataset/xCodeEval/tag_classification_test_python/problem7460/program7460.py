    #!/usr/bin/python
    
    import sys
    import math
    
def read_obj(cls):
        return cls(sys.stdin.readline().strip())
    
def read_obj_list(cls):
        return map(cls, sys.stdin.readline().strip().split())
    
    
def solve():
        n = read_obj(int)
        res = [1, 0 ,18, 0, 1800, 0, 670320, 0 ,734832000, 0, 890786230, 0, 695720788, 0, 150347555, 0]
        return res[n-1]
    
    
    if __name__ == "__main__":
        print(solve())