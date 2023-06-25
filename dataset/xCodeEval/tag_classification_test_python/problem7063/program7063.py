    import atexit
    import io
    import sys
    import math
    
    # Buffering IO
    _INPUT_LINES = sys.stdin.read().splitlines()
    input = iter(_INPUT_LINES).__next__
    _OUTPUT_BUFFER = io.StringIO()
    sys.stdout = _OUTPUT_BUFFER
    
    @atexit.register
def write():
        sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
        
    
def main():
        n = int(input())
        ss = 0
        
        k = 1
        while n>1:
            ss += k * (n // 2)
            n = math.ceil(n/2)
            k*=2
        
        print(ss)
    
        
    if __name__ == '__main__':
        main()
            