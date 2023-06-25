    import random
    import time
    
    seed = int(time.time())
    random.seed(seed)
    
def solve():
        pass
    
def main():
        S = input().strip()
        iS = int(S, 2)
        acc = 0
        for k in range(55):
            acc += iS > 4**k
        print(acc)
    
    if '__main__'==__name__:
        main()