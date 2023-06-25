def solver():
        r,h = map(int, input().split())
        ans = 2 * (h/r)
        x = h % r
        if 4 * x * x >= 3 *r * r:
            ans += 3
        elif 2 * x >= r:
            ans += 2
        else:
            ans += 1
    
        print(ans)
    
    
    if __name__ == "__main__":
        solver()