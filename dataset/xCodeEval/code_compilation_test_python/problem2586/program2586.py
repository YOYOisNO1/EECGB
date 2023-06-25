    n = 0
    arr = []
    
def log(func):
    def f(*args):
            res = func(*args)
            print(f'{func.__name__}({args}) = {res}')
            return res
        
        return f
    
    
    # @log
def check1(i, j):
        # assert (j - i) % 2 == 1
        return not (arr[i] % 2 == 0 or arr[j - 1] % 2 == 0)
    
    # @log
def check2(i, j):
        # assert (j - i) % 2 == 0
        for k in range(i + 1, j, 2):
            if check1(i, k) and check1(k, j):
                return True
    
        for k in range(i + 2, j - 1, 2):
            if check2(i, k) and check2(k, j):
                return True
        
        return False
    
def main():
        global n
        global arr
        n = int(input())
        arr = list(map(int, input().split(' ')))
    
        if n % 2 == 0:
            return False
    
        return check1(0, n)
    
    
    if main():
        print('Yes')
    else:
        print('No')