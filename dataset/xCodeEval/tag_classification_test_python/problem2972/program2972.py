def readints():
        return [int(obj) for obj in input().strip().split()]
    
    
    class Solver:
    def main(self):
            n = readints()[0]
            a = readints()
            f = [0] * n
    
            f[n - 1] = a[n - 1]
            for i in range(n - 2, -1, -1):
                f[i] = max(
                    sum(a[i:n]) - f[i+1],
                    f[i+1],
                )
            print(sum(a) - f[0], f[0])
    
    
    Solver().main()