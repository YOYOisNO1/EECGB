def digits(w, m):
        while m >= w:
            m, d = divmod(m, w)
            yield d
        yield m
    
    
def scale(w, m):
        if w <= 3:
            return True
        c = 0
        for d in digits(w, m):
            # log('d', d, 'c', c)
            d = d + c
            if d in (0, 1):
                c = 0
            elif d in (w, w-1):
                c = 1
            else:
                return False
        return True
    
def main():
        w, m = readinti()
        print('YES' if scale(w, m) else 'NO')
    
    ##########
    
    import sys
    import time
    import traceback
    from contextlib import contextmanager
    from io import StringIO
    
def readint():
        return int(input())
    
    
def readinti():
       return map(int, input().split())
    
    
def readintl():
       return list(readinti())
    
    
def readintll(k):
        return [readintl() for _ in range(k)]
    
    
def log(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
    
    
    @contextmanager
def patchio(i):
        try:
            sys.stdin = StringIO(i)
            sys.stdout = StringIO()
            yield sys.stdout
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
    
    
def do_test(k, test):
        try:
            log(f"TEST {k}")
            i, o = test
            with patchio(i) as r:
                t0 = time.time()
                main()
                t1 = time.time()
            if r.getvalue() == o:
                log(f"OK ({int((t1-t0)*1000000)/1000:0.3f} ms)\n")
            else:
                log(f"Expected:\n{o}"
                    f"Got ({int((t1-t0)*1000000)/1000:0.3f} ms):\n{r.getvalue()}")
        except Exception:
            traceback.print_exc()
            log()
    
    
def test(ts):
        for k in ts or range(len(tests)):
            do_test(k, tests[k])
    
    
    tests = [("""\
    3 7
    """, """\
    YES
    """), ("""\
    100 99
    """, """\
    YES
    """), ("""\
    100 50
    """, """\
    NO
    """)]
    
    
    if __name__ == '__main__':
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('--test', '-t', type=int, nargs='*')
        args = parser.parse_args()
        main() if args.test is None else test(args.test)