 def res(n, k):
         max_res = min(n, k - 1)
         min_res = max(1, k - max_res)
         return max(0, (max_res + 1 - min_res) // 2)
    a = int(input())
    b = int(input())
    print(res(a,b))