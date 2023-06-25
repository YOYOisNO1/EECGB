def main():
    def ch(n):
            d = 2
            s = set()
            while n != 1:
                if n % d == 0:
                    n = n // d
                    s.add(d)
                else:
                    d += 1
            return len(s)
    
        n = int(input())
        cnt = 0
        for i in range(1, n+1):
            if ch(i) == 2:
                cnt += 1
        print(cnt)
    
    
    if __name__ == '__main__':
        main()