def program156():
    
    if __name__ == "__main__":
        a, b = map(int, input().split())
        c, d = map(int, input().split())
    
        res = None
        for y in range(1000):
            if b > d:
                if ((b - d) + y * a) % c == 0:
                    res = b + y * a
                    break
            else:
                if ((d - b) + y * c) % a == 0:
                    res = d + y * c
                    break
    
        if res:
            print(res)
        else:
            print(-1)
    