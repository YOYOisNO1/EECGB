    import os
    from sys import stdin, stdout
    
    class Input:
    def __init__(self):
            self.lines = stdin.readlines()
            self.idx = 0
        
    def line(self):
            try:
                return self.lines[self.idx].strip()
            finally:
                self.idx += 1
        
    def array(self, sep = ' ', cast = int):
            return list(map(cast, self.line().split(sep = sep)))
        
    def has_next(self):
            return self.idx < len(self.lines)
    
def known_cases(func):
        inpt = Input()
        cases, = inpt.array()
        for case in range(cases):
            func(inpt)
    
def unknown_cases(func):
        inpt = Input()
        while inpt.has_next():
            func(inpt)
    
    '''
    HAPPY CODING
    '''
    
    import math
    
    @unknown_cases
def solve(inpt):
        '''E. Rock, Paper, Scissors'''
        n, = inpt.array()
        a = inpt.array()
        b = inpt.array()
    
        mx = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    
        mn = [
            min(a[0] - (n - b[1]), b[1]),
            min(a[1] - (n - b[2]), b[2]),
            min(a[2] - (n - b[0]), b[0])
        ]
    
        print(max(0, *mn), mx)