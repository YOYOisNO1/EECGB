    from sys import *
    from bisect import *
    from collections import *
    from itertools import *
    from fractions import *
    
    Input = []
    
    #stdin = open('in', 'r')
    #stdout = open('out', 'w')
    
    ## for i, val in enumerate(array, start_i_value)
    
def Out(x):
        stdout.write(str(x) + '\n')
    
def In():
        return stdin.readline().strip()
    
def inputGrab():
        for line in stdin:
            Input.extend(map(str, line.strip().split()))
    '''--------------------------------------------------------------------------------'''
    
def Search(target, Y):
        low = 0
        hi = 100009
        Min = 1000000.
        ANS = 0
        
        for i in range(80):
            X = (low+hi)//2
            
            if(abs(X/Y-target) <= Min):
                Min = abs(X/Y-target)
                ANS = X
            
            if(X/Y <= target):
                low = X+1
            else:
                hi = X-1
        
        return ANS
    
    
def main():
        x, y, n = map(int, In().split())
        
        ansX = 0
        ansY = 0
        Min = Fraction(100000, 100000)
        
        for Y in range(1, n+1):
            X = Search(x/y, Y)
            
            Dist = abs(Fraction(X, Y) - Fraction(x, y))
            
            if(Dist < Min):
                ansX = X
                ansY = Y
                Min = Dist
                
            
            #print(X, Y, X/Y, abs(X/Y - x/y), Min)
        
        print(str(ansX)+"/"+str(ansY))
        
    if __name__ == '__main__':
        main()