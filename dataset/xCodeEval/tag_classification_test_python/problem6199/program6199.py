def main():
        r1, c1, r2, c2 = map(int, input().split())
        print((r1 != r2) + (c1 != c2),
              0 if (r1 + r2 + c1 + c2) & 1 else 1 if abs(r1 - r2) == abs(c1 - c2) else 2,
              max(abs(r1 - r2), abs(c1 - c2)))
    
    
    if __name__ == '__main__':
        main()