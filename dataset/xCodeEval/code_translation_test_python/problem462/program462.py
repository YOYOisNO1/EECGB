def solve(n, arr):
        if n % 2 == 0 or arr[0] % 2 == 0 or arr[-1] % 2 == 0:
            return False
        return True
    
    if __name__ == "__main__":
        n = input()
        arr = map(int, input().split())
        if solve(n, arr):
            print('Yes')
        else:
            print('No')