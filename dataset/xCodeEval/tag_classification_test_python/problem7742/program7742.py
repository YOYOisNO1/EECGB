def main():
        n = int(input())
        a = map(int, input().split())
        a.sort()
        if n == 1:
            print("BitLGM") if a[0] else "BitAryo"
        elif n == 3:
            print("BitLGM") if a[0] ^ a[1] ^ a[2] else "BitAryo"
        else:
            d = set([(0, 0)])
            g = set()
            g.add(0)
            prev = [0, 0]
            i = 1
            while i < 300:
                if i not in g:
                    prev[1] += i - prev[0] + 1
                    prev[0] = i
                    d.add(tuple(prev))
                    g.add(prev[0])
                    g.add(prev[1])
                i += 1
            print("BitLGM") if tuple(a) not in d else "BitAryo"
    main()