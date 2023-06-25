def solve(n):
        ans = 0
        while True:
            for i in range(len(n)):
                ans += int(n[i])
    
            if ans%4 == 0:
                print(n)
                break
            else:
                ans = 0
                n = int(n) + 1
                n = str(n)
    
        return
    
    if __name__ == '__main__':
        n = input()
    
        solve(n)