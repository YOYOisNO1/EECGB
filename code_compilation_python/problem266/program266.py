    import sys
    import math
    
    
def readlines(type=int):
        return list(map(type, sys.stdin.readline().split()))
    
    
def read(type=int):
        return type(sys.stdin.readline().strip())
    
    
    joint = lambda it, sep=" ": sep.join(
        [str(i) if type(i) != list else sep.join(map(str, i)) for i in it])
    
    
def solve(n, t, k, d):
        n_mul = (n * t) // k + 1
        t_muls = set()
        for i in range(1, n_mul + 1):
            t_muls.add(t * i)
            t_muls.add((t * i) + d)
        t_muls = sorted(list(t_muls))
        for mul in t_muls:
            yeild = k * ((mul // t) + (mul - d) // t)
            if yeild >= n:
                # mulc = mul
                break
        # print(t_muls)
        # print(mul, f"{t * math.ceil(n / k)=}", n, k, t)
        if mul < t * math.ceil(n / k):
            return "YES"
        return "NO"
    
    
def main():
        print(solve(*readlines()))
    
    
    if __name__ == "__main__":
        main()