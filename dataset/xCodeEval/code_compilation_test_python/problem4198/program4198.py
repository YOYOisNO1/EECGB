    import time
    
    
def sort(n, s):
        a = list(range(1, n + 1))
        px = [0]
        b = [0] * n
    
    def mergeSort(l, r):
            m = (l + r) >> 1
    
            if m - l > 1:
                ans = mergeSort(l, m)
                if ans == -1:
                    return -1
            if r - m > 1:
                ans = mergeSort(m, r)
                if ans == -1:
                    return -1
            i, j, k = l, m, l
            while i < m and j < r:
                if px[0] >= len(s):
                    return -1
    
                if s[px[0]] == '0':
                    b[k] = a[i]
                    i += 1
                else:
                    b[k] = a[j]
                    j += 1
                k += 1
                px[0] += 1
            while i < m:
                b[k] = a[i]
                i += 1
                k += 1
            while j < r:
                b[k] = a[j]
                j += 1
                k += 1
    
            for p in range(l, r):
                a[p] = b[p]
    
        ans = mergeSort(0, n)
        if ans == -1:
            return -1
        if px[0] != len(s):
            return 1
        return a
    
    
def main():
        d_min = {0: [], 1: [], 2: [1]}
        d_max = {0: [], 1: [], 2: [1]}
    
    def get_min(n):
            if n not in d_min:
                d_min[n] = [n // 2] + get_min(n - n // 2) + get_min(n // 2)
    
            return d_min[n]
    
    def get_max(n):
            if n not in d_max:
                d_max[n] = [n - 1] + get_max(n - n // 2) + get_max(n // 2)
    
            return d_max[n]
    
        s = input()
        # lens = len(s)
        # l, r = 1, 10 ** 3 + 1
        # while r - l > 1:
        #     m = (l + r) // 2
        #     if sum(get_min(m)) > lens:
        #         r = m
        #     else:
        #         l = m
        # max_n = l
        #
        # l, r, = 1, 10 ** 3 + 1
        # while r - l > 1:
        #     m = (l + r) // 2
        #     if sum(get_max(m)) < lens:
        #         l = m
        #     else:
        #         r = m
        # min_n = r
    
        for n in range(16, 0, -1):
            ans = sort(n, s)
            if isinstance(ans, list):
                out = [''] * n
                print(n)
                for i, aa in enumerate(ans):
                    out[aa - 1] = str(i + 1)
                print(' '.join(out))
                break
    
    
    ############
    
def i_input():
        return int(input())
    
    
def l_input():
        return input().split()
    
    
def li_input():
        return list(map(int, l_input()))
    
    
def il_input():
        return list(map(int, l_input()))
    
    
    # endregion
    
    if __name__ == "__main__":
        TT = time.time()
        main()
        # print("\n", time.time() - TT)