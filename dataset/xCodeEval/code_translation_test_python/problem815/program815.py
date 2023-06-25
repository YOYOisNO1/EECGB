def main():
        n, m = map(int, input().split())
        a, *aa = map(int, input().split())
        c, res = 1 - (a & 1) * 2, []
        for b in aa:
            if not c:
                res.append(abs(a - b))
            if b & 1:
                c -= 1
            else:
                c += 1
            a = b
        for i, a in enumerate(sorted(res)):
            if m < a:
                print(i)
                return
            m -= a
        print(len(res))
    
    
    if __name__ == '__main__':
        main()