def solution():
        n = int(input())
        ans = 1
        p = 2
        nxt = 3
        while True:
            if n < nxt:
                return ans
            p, nxt = nxt, p + nxt
            ans += 1
    
    if __name__ == '__main__':
        print(solution())