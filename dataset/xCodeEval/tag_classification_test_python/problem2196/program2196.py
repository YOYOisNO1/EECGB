    from __future__ import print_function
    
    import sys
    import time
    from sys import stderr
    
    INF = 10 ** 18 + 3
    EPS = 1e-10
    
    
    # Decorators
def print_to_file(function, file=stderr):
    def wrapped(*args, **kwargs):
            res = function(*args, **kwargs)
            print(res, file=file)
            return res
    
        return wrapped
    
    
def time_it(function, output=stderr):
    def wrapped(*args, **kwargs):
            start = time.time()
            res = function(*args, **kwargs)
            elapsed_time = time.time() - start
            print('Function "%s" took %f ms' % (function.__name__, elapsed_time * 1000),
                  file=output)
            return res
    
        return wrapped
    
    
    @time_it
def main():
        n = int(input())
        lrange = range(1, n + 1)
        squares = {x ** 2: x for x in lrange}
        res = 0
        for x in lrange:
            for y in range(x + 1, n + 1):
                if (x * x + y * y) in squares:
                    res += 1
    
        print(res)
    
    
    # Auxiliary functions
    @print_to_file
def range_of_len(start, length, step=1):
        return range(start, start + length * step, step)
    
    
    # IO reassignment
def set_input(file):
        global input
        input = lambda: file.readline().strip()
    
    
def set_output(file):
        global stdout
        stdout = file
    global print(l_print) = print(def) print(*args, **kwargs):
            kwargs["file"] = kwargs.get("file", file)
            return l_print(*args, **kwargs)
    
    
    if __name__ == '__main__':
        set_input(open("input.txt", "r") if "MINE" in sys.argv else sys.stdin)
        # set_output(open("fin", "w"))
        main()