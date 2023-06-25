    class A:
    def __init__(self):
            self.count = 0
            self.sz = 0
    
    def find_binary_rep(self, num):
            if num > 0:
                k, r = divmod(num, 2)
                self.sz += 1
                self.find_binary_rep(k)
    
    def count_ones(self, num, l, r, i, j):
            if l > j or r < i:
                return
            elif l <= i <= r and l <= j <= r:
                self.count += num
            elif num > 1:
                k = num // 2
                m = (i+j-1)//2
                self.count_ones(k, l, r, i, m)
                if l <= m+1 <= r:
                    self.count += num % 2
                self.count_ones(k, l, r, m + 2, j)
    
    
    if __name__ == "__main__":
        n, left, right = tuple(map(int, input().split()))
        a = A()
        a.find_binary_rep(n)
        total_sz = 2**a.sz - 1
        # print(total_sz)
        a.count_ones(n, left, right, 1, total_sz)
        print(a.count)