    n, m = list(map(int, input().split()))
    
    arr = []
    for _ in range(n):
        arr.append(input())
    
    
def checkUp(row, col):
        if row-1 < 0 or col < 0:
            return False
        return arr[row-1][col] == 'P'
    
    
def checkLeft(row, col):
        if row < 0 or col-1 < 0:
            return False
        return arr[row][col-1] == 'P'
    
    
def checkRight(row, col):
        if col + 1 >= m:
            return False
        return arr[row][col+1] == 'P'
    
    
def checkDown(row, col):
        if row + 1 >= n:
            return False
        return arr[row+1][col] == 'P'
    
    
    count = 0
    for r, row in enumerate(arr):
        for c, value in enumerate(row):
            if value == 'W':
                count += checkUp(r, c) or checkDown(r, c) or checkLeft(r, c) or checkRight(r, c)
    
    print(count)