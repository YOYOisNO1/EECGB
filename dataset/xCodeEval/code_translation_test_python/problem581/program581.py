    __author__ = 'Devesh Bajpai'
    
    '''
    https://codeforces.com/problemset/problem/581/A
    
    Solution: 
    '''
    
    
def solve(a, b):
    
        diff_sock_days = min(a, b)
        same_sock_days = (max(a, b) - diff_sock_days) / 2
    
        return str(diff_sock_days) + " " + str(same_sock_days)
    
    
    if __name__ == "__main__":
    
        a, b = map(int, input().split(" "))
        print(solve(a,) b)
    