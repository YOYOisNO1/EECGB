    __author__ = 'Darren'
    
    
def solve():
        n, h = map(int, input().split())
        dp1, dp2 = {}, {}
    
    def trees(nodes):
            nonlocal dp1
            if nodes < 0:
                return 0
            if nodes < 2:
                return 1
            if nodes not in dp1:
                count = 0
                for i in range(nodes):
                    count += trees(i) * trees(nodes-i-1)
                dp1[nodes] = count
            return dp1[nodes]
    
    def trees_with_height_limit(nodes, height):
            nonlocal dp2
            if nodes < 0 or height <= 0 or nodes >= 2 ** (height - 1):
                return 0
            if nodes < 2:
                return 1
            if nodes < height:
                return trees(nodes)
            if (nodes, height) not in dp2:
                count = 0
                for i in range(nodes):
                    count += (trees_with_height_limit(i, height-1) *
                              trees_with_height_limit(nodes-i-1, height-1))
                dp2[nodes, height] = count
            return dp2[nodes, height]
    
        print(trees(n) - trees_with_height_limit(n, h))
    
    
    if __name__ == '__main__':
        solve()