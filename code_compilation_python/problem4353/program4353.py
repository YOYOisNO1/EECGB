    from sys import stdin, setrecursionlimit
    from collections import *
    import threading
    
    
def arr_inp(n):
        if n == 1:
            return [int(x) for x in stdin.readline().split()]
        elif n == 2:
            return [float(x) for x in stdin.readline().split()]
        else:
            return list(stdin.readline()[:-1])
    
    
def dp(i, rem):
        if rem == 0:
            return 0
        if i >= len(arr):
            if rem:
                return d0 * (rem // c0)
            else:
                return 0
    
        if mem[i][rem] != -1:
            return mem[i][rem]
    
        ans1, ans2, ans3 = dp(i + 1, rem), 0, 0
    
        if rem - arr[i][0] >= 0:
            ans2 = arr[i][1] + dp(i + 1, rem - arr[i][0])
        if rem - c0 >= 0:
            ans3 = d0 + dp(i + 1, rem - c0)
    
        mem[i][rem] = max(ans1, ans2, ans3)
        return mem[i][rem]
    
    
def main():
        print(dp(0, n))
    
    
    if __name__ == '__main__':
        n, m, c0, d0 = arr_inp(1)
        staff, arr, mem = [arr_inp(1) for i in range(m)], [], [[-1 for i in range(1001)] for j in range(1001)]
    
        for a in staff:
            arr.extend([[a[2], a[3]] for i in range(a[0] // a[1])])
    
        setrecursionlimit(200000)
        threading.stack_size(102400000)
        thread = threading.Thread(target=main)
        thread.start()