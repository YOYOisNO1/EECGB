    import collections
    
def main():
        n, k = map(int, input().split(" "))
    
        n = list(str(n))
        c = collections.Counter(n)
        if c['0'] < k:
            print(len(n)) - 1
            return
    
        badCounter, zeroCounter = 0, 0
        for i in xrange(len(n) - 1, -1, -1):
            if n[i] == '0':
                zeroCounter += 1
            if n[i] != '0':
                badCounter += 1
            if zeroCounter == k:
                print(badCounter)
                return
        if zeroCounter == k:
            print(badCounter)
            return
    
    if __name__ == "__main__":
        main()