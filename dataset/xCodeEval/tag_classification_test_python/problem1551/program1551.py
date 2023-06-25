def solve(lis, x, y):
    def check(a, b):
            return a>=x and a<=y and b>=x and b<=y
        a = sum(lis)
        b = 0
        for i in xrange(len(lis)-1):
            a -= lis[i]
            b += lis[i]
            if(check(a, b)):
                return i+2
        return 0
    
def main():
        _ = input()
        lis = map(int, input().split())
        [x, y] = map(int, input().split())
        print(solve(lis,) x, y)
    if __name__ == "__main__":
        main()