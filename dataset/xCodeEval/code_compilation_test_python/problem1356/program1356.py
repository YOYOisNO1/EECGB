    import sys
    import time
    import math
    from collections import defaultdict
    from functools import lru_cache
    
    INF = 10 ** 18 + 3
    EPS = 1e-10
    MAX_CACHE = 10 ** 12
    
    
def time_it(function, output=sys.stderr):
    def wrapped(*args, **kwargs):
            start = time.time()
            res = function(*args, **kwargs)
            elapsed_time = time.time() - start
            print('"%s" took %f ms' % (function.__name__, elapsed_time * 1000),
                  file=output)
            return res
    
        return wrapped
    
    
    @lru_cache(MAX_CACHE)
def find_possible_heights(n):
        res = 0
        curr_level = 1
        while True:
            if n % 3 == 2 and n > curr_level * 3 - 4:
                res += 1
            n -= curr_level * 3 - 1
            curr_level += 1
            if n <= 0:
                return res
    
    
    @time_it
def main():
        n = int(input())
        print(find_possible_heights(n))
    
    
def set_input(file):
        global input
        input = lambda: file.readline().strip()
    
    
def set_output(file):
        global print
        local_print = print
    
    def print(*args, **kwargs):
            kwargs["file"] = kwargs.get("file", file)
            return local_print(*args, **kwargs)
    
    
    if __name__ == '__main__':
        set_input(open("input.txt", "r") if "MINE" in sys.argv else open("input.txt", "w"))
        set_output(sys.stdout)
        main()