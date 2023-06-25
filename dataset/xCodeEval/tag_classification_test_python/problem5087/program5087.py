def ans(arr):
        cnt_1 = arr.count(1)
        cnt_2 = n - cnt_1
        cnt = 0
        i = 0
        while i < k:
            cnt1, cnt2 = 0, 0
            j = i
            while j < n:
                if(arr[j] == 1):
                    cnt1 += 1
                else:
                    cnt2 += 1
                j += k
            cnt = max(cnt, abs((cnt_1 - cnt1) - (cnt_2 - cnt2)))
            i += 1
        return cnt
    
    if __name__ == '__main__':
        nk = list(map(int, input().strip().split()))
        n, k = nk[0], nk[1]
        a = list(map(int, input().strip().split()))
        print(ans(a))