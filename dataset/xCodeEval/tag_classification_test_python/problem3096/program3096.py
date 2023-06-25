    import sys
    class IoTool:  # a tool for input redirection 
        DEBUG = 0
    def _reader_dbg():
            with open('./input.txt', 'r') as f:
                lines = f.readlines()
            for l in lines: yield l.strip() 
    def _reader_oj():  
            return iter(sys.stdin.read().split('\n'))
        reader = _reader_dbg() if DEBUG else _reader_oj()
    def read(): return next(IoTool.reader)
    
    input = IoTool.read
    MOD = 998244353
    
def main():
        n, m, l, r = map(int, input().split())
        if (n * m) & 1 == 1:
            print(pow(r-l+1, m * n, MOD))
        else:
            odd = (r + 1) // 2 - l // 2
            even = r // 2 - (l-1) // 2
            tmp = (pow(even + odd, m*n, MOD) + pow(even - odd, m*n, MOD) + MOD) % MOD
            print(tmp * pow(2, MOD-2, MOD) % MOD)
    
    if __name__ == "__main__":
        main()