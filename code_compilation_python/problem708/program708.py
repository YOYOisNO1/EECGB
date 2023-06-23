def main():
        n = int(input())
        div, mod = divmod(n, 3)
        ans = mod
    
        div, mod = divmod(div)
        ans += mod + div
    
        print(ans)
    
    
    if __name__ == "__main__":
        main()