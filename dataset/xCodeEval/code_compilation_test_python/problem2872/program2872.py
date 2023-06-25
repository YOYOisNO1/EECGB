    from time import time
    from collections import defaultdict
    
def main():
        begin = time()
        N = int(1e4)
        f = [0] * N
        #f = defaultdict(int)
        for i in range(N):
            for j in range(N):
                f[i] += i * j
        #for i in range(int(1e8)):
        #    a = i * i
        print(time()-begin)
    
    main()