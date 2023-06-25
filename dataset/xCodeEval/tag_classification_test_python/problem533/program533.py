def readints():
        return [int(item) for item in input().strip().split()]
    
    
    class Solver:
    def main(self):
            n, k = readints()
            a = readints()
            items = [1] * (k + 1)
            items[k] = 0
    
            for i in a:
                if i < k:
                    items[i] = 0
                if i == k:
                    items[i] = 1
    
            print(sum(items))
    
    
    Solver().main()