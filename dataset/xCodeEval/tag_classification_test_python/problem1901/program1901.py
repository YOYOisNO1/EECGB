    import math
    
    
def main():
        x, y = map(int,  input().split())
        if x > 0 and y > 0:
            c =[(x+y, 0), (0, x+y)]
            print(*min(c), *max(c))
        if x > 0 and y < 0:
            c = [(x - y, 0), (0, -(x - y))]
            print(*min(c), *max(c))
        if x < 0 and y > 0:
            c = [(-(-x + y), 0), (0, -x + y)]
            print(*min(c), *max(c))
        if x < 0 and y < 0:
            c = [(-(-x - y), 0), (0, -(-x - y))]
            print(*min(c), *max(c))
    
    
    if __name__ == '__main__':
        main()