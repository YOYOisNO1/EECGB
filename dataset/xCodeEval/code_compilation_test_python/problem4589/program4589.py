def check(ds, k):
        while any(ds):
            s = 0
            for i in range(len(ds)):
                s += ds[i] % 2
                ds[i] /= 2
            s %= k + 1
            if s:
                return True
        return False
    
def main():
        n, m, k = map(int, input().split())
        A = B = False
        ds = []
        for i in range(n):
            line = input().strip()
            a = line.find('R')
            b = line.find('G')
            if a != -1 and b != -1:
                ds.append(abs(a - b))
            elif a != -1 and b == -1:
                A = True
            elif a == -1 and b != -1:
                B = True
        if A and B:
            print 'Draw'
        elif A:
            print 'First'
        elif B:
            print 'Second'
        else:
            print 'First' if check(ds, k) else 'Second'
    
    if __name__ == '__main__':
        main()