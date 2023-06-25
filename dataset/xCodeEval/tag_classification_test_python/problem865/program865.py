    from sys import stdin, setrecursionlimit
    
    
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
        ans = 0
        for j in range(len(arr)):
            mem[j][n] = 0
    
        if arr:
            if n - arr[0][0] >= 0:
                mem[0][n - arr[0][0]] = arr[0][1]
    
            for j in range(1, len(arr)):
                for i in range(n + 1):
                    mem[j][i] = mem[j - 1][i]
    
                    if i + arr[j][0] <= n:
                        if mem[j - 1][i + arr[j][0]] != -1:
                            mem[j][i] = max(mem[j][i], mem[j - 1][i + arr[j][0]] + arr[j][1])
                            ans = max(ans, mem[j][i])
    
        # print(dp(0, n))
        for j in range(len(arr) + 1):
            for i in range(n, -1, -1):
                ext = (i // c0) * d0
                if mem[j][i] == -1:
                    mem[j][i] = ext
                else:
                    mem[j][i] += ext
                ans = max(ans, mem[j][i])
        print(ans)
    
    
    if __name__ == '__main__':
        n, m, c0, d0 = arr_inp(1)
        staff, arr = [arr_inp(1) for i in range(m)], []
    
        for a in staff:
            arr.extend([[a[2], a[3]] for i in range(a[0] // a[1])])
    
        mem = [[-1 for i in range(n + 1)] for j in range(len(arr) + 1)]
        main()