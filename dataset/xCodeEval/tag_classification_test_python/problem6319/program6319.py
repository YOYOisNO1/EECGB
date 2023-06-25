    #!/usr/bin/env python
    
def main():
        a, b = [int(c) for c in input().split()]
        div, mod = divmod(b - a, 10)
        cnt = [div] * 10
        for i in range(mod):
            cnt[(a + 1 + i) % 10] += 1
    
        # 0: 0
        # 1: 1
        # 2: 2 4 8 6
        # 3: 3 9 7 1
        # 4: 4 6
        # 5: 5
        # 6: 6
        # 7: 7 9 3 1
        # 8: 8 4 2 6
        # 9: 9 1
    
        change = {0: [0], 1:[1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6],
                  5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 6, 2], 9: [9, 1]}
    
        res = 1
        no_change = {0, 1, 5, 6, 9}
        for i, c in enumerate(cnt):
            if c > 0:
                cc = change[i]
                res *= cc[c % len(cc) - 1]
    
        print(res % 10)
            
    if __name__ == '__main__':
        main()