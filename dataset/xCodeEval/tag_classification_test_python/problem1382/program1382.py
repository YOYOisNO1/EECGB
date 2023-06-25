def main():
        n = int(input())
        lookup = set()
        k = 1
        while k * (k + 1) // 2 <= n:
            lookup.add(k * (k + 1) // 2)
            k += 1
    
        ok = False
        for elm in lookup:
            if elm < n:
                if n - elm in lookup:
                    ok = True
        if ok:
            print("YES")
        else:
            print("NO")
    
    
    if __name__ == "__main__":
        main()