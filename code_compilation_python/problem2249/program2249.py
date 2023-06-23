def main():
        a, b, c, d = map(int, input().split())
        c, d = c-a, d-b
        x, y = map(int,input.().split())
        
        if c%x != 0 or d%y != 0:
            print("NO")
        elif c/x % 2 == d/y %2:
            print("YES")
        else:
            print("NO")
    
    if __name__ == "__main__":
        main()