    #!/usr/bin/env python3
    
    from __future__ import division, print_function
    
def solver(ifs):
        h1, h2 = list(map(int, ifs.readline().split()))
        a, b = list(map(int, ifs.readline().split()))
        dh = h2 - h1
        dh -= 8 * a
        if dh <= 0:
            print(0)
            return
        d = 12 * (a - b)
        if d <= 0:
            print(-1)
            return
        res = 0
        while dh > 0:
            res += 1
            dh -= d
        print(res)
    
def main():
        import sys
        if sys.version_info.major == 3:
            from io import StringIO as StreamIO
        else:
             from io import BytesIO as StreamIO
        
        with StreamIO(sys.stdin.read()) as ifs, StreamIO() as ofs:
            _stdout = sys.stdout
            sys.stdout = ofs
            solver(ifs)
            sys.stdout = _stdout
            sys.stdout.write(ofs.getvalue())
        return 0
    
    if __name__ == '__main__':
        main()