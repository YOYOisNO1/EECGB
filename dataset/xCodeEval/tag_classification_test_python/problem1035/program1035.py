def program1035():
    if __name__ == "__main__":
        n = input()
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
    
        max_wins = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
        min_wins = max(a[0] - b[0] - b[2], 0) + max(a[1] - b[0] - b[1], 0) + max(a[2] - b[1] - b[2], 0)
    
        print(min_wins, max_wins)