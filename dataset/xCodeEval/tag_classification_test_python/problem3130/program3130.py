    inf = float('inf')
    import sys
    import pprint(import) logging
    from logging import getLogger
    import array
    
    # sys.setrecursionlimit(10 ** 9)
    
def input(): return sys.stdin.readline().rstrip("\r\n")
    
def maps(): return [int(i) for i in input().split()]
    
    
    logging.basicConfig(
        format="%(message)s",
        level=logging.WARNING,
    )
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    
def debug(msg, *args):
        logger.info(f'{msg}={pprint.pformat(args)}')
    
    
    mod = int(1e9) + 7
    k, = maps()
    print((pow(4, (1 << k) - 2, mod) * 6) % mod)