def main():
        from collections import Counter
        n = int(input())
        if n == 1:
            print(input())
            return
        cnt = Counter({"R": 0, "G": 0, "B": 0})
        cnt.update(input())
        r, g, b = sorted("RGB", key=cnt.get)
        print(''.join(sorted("RGB" if cnt[r] else (r if n == 2 else r + g) if cnt[g] == 1 else "RGB" if cnt[g] else b)))
    
    
    if __name__ == '__main__':
        main()