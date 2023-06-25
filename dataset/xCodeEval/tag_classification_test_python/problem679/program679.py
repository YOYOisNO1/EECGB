def program679():
    if __name__ == "__main__":
        n, m = list(map(int, input().split()))
    
        if n == 0:
            if m == 0:
                print(0, 0)
            else:
                print("Impossible")
        elif m == 0:
            print(n, n)
        elif n >= m:
            print(n, n + m -1)
        else:
            print(n + m - n, n + m - 1)