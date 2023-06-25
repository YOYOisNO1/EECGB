def main():
        n, m = map(int, input().split())
        s, l = input(), []
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            i = s.find(c)
            if i != -1:
                l += (((i, -1), (s.rfind(c), 1)))
        for _, i in sorted(l):
            m += i
            if m < 0:
                print('YES')
                return
        print('NO')
    
    
    if __name__ == '__main__':
        main()