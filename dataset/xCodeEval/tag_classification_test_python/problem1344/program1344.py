    
    
def game(n, k1, K1, k2, K2):
        # Dumb brute force approach
        seen = set()
        P1 = tuple(K1)
        P2 = tuple(K2)
        turns = 0
        while True:
            if not P1:
                return turns, 2
            if not P2:
                return turns, 1
    
            state = P1, P2
            if state in seen:
                return -1, None
            seen.add(state)
    
            if P1[0] > P2[0]:
                P1 = P1[1:] + (P2[0], P1[0])
                P2 = P2[1:]
            else:
                P2 = P2[1:] + (P1[0], P2[0])
                P1 = P1[1:]
    
            turns += 1
    
    
def main():
        n = readint()
        k1, *K1 = readinti()
        k2, *K2 = readinti()
        turns, winner = game(n, k1, K1, k2, K2)
        print(f"{turns} {winner}" if turns >= 0 else "-1")
    
    
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
    4
    2 1 3
    2 4 2
    """, """\
    6 2
    """),("""\
    3
    1 2
    2 1 3
    """, """\
    -1
    """)]
    
    
    if __name__ == '__main__':
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('--test', '-t', type=int, nargs='*')
        args = parser.parse_args()
        main() if args.test is None else test(args.test)