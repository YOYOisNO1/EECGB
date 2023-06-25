def cronch(A):
        D = {v:i for i, v in enumerate(sorted(set(A)))}
        return len(D), [D[a] for a in A]
    
    
def lnds(n, t, A):
        m, A = cronch(A)
        S = [[0 for _ in range(m)] for _ in range(m)]
        for j in A:
            for i in range(j+1):
                S[i][j] += 1
                v = S[i][j]
                for k in range(j+1, m):
                    if S[i][k] >= v:
                        break
                    S[i][k] = v
    
        # for r in S:
        #     log(r)
    
        # log()
    
        if t <= 2 * m:
            V = [0 for _ in range(m)]
            for _ in range(t):
                V2 = [0 for _ in range(m)]
                for i in range(m):
                    for j in range(i, m):
                        V2[j] = max(V2[j], V[i] + S[i][j])
                V = V2
                # log(V)
            return max(V)
        else:
            V = [0 for _ in range(m)]
            W = [0 for _ in range(m)]
            for _ in range(m):
                V2 = [0 for _ in range(m)]
                W2 = [0 for _ in range(m)]
                for i in range(m):
                    for j in range(i, m):
                        V2[j] = max(V2[j], V[i] + S[i][j])
                        W2[i] = max(W2[i], S[i][j] + W[j])
                V = V2
                W = W2
                # log(V, W)
    
            p = t - (2*m)
            return max(V[k] + S[k][k]*p + W[k] for k in range(m))
    
    
def main():
        n, t = map(int, input().split())
        A = list(map(int, input().split()))
        assert len(A) == n
        print(lnds(n, t, A))
    
    ##########
    
    import sys
    import time
    import traceback
    from contextlib import contextmanager
    from io import StringIO
    
    
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
    4 3
    3 1 4 2
    """, """\
    5
    """)]
    
    
    if __name__ == '__main__':
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument('--test', '-t', type=int, nargs='*')
        args = parser.parse_args()
        main() if args.test is None else test(args.test)