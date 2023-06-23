    #coding:utf-8
    import os
    import sys
    
    f = None
def readLine():
        global f
        if len(os.environ) == 63:
            if not f:
                f = open("a.txt")
            return f.readline()
        else:
            return input()
    
    
    if __name__ == '__main__':
        print min([x/y for x, y in zip(map(int, readLine().split()), [1, 1, 2, 7, 4])])