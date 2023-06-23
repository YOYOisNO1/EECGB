def main():
        n = int(input()) + 1
        if n == 1:
            print("4\n1 2 3 4")
            return
        p, l = 5, [1] * n
        while p < n:
            for i in range(p, n + 1, p):
                l[i] += 1
            p *= 5
        p = 0
        for i, a in enumerate(l):
            p += a
            if p == n:
                print(5)
                print(*range(i * 5, i * 5 + 5))
                return
        print(0)
    
    
    if __name__ == '__main__':
        main()