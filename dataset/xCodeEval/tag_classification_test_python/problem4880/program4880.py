def main():
        n, k = map(int, input().split())
    
        if n - (k - 2 * n) > 0:
            print(n) - (k - 2 * n)
        else:
            print(0)
        
    if __name__ == "__main__":
        main()