def read_input():
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])
        d = int(line[2])
        print(calculate(n, k, d, {}) % (10**9 + 7))
    
def calculate(n, k, d, memo):
        if (n, d) in memo:
            return memo[(n, d)]
        else:
            if (n, d) == (0, 0):
                return 1
            x = 0
            if d == 0:
                i = 1
                while n - i >= 0 and i <= k:
                    x += calculate(n-i, k, 0, memo)
                    i += 1
            else:
                for i in range(1, k+1):
                    if i >= d:
                        x += calculate(n-i, k, 0, memo)
                    elif n >= i + d:
                        x += calculate(n-i, k, d, memo)
            memo[(n, d)] = x
            return x
    
    if __name__ == "__main__":
        read_input()