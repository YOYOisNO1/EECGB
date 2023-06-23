    from time import time
    from collections import defaultdict
    
def main():
        begin = time()
        N = int(1e4)
        f = [0] * N
        for i in range(N):
            for j in range(N):
                f[i] += j
        print(time()-begin)
    
    main()