    import bisect
    
def ni():
        return int(input())
    
def nis():
        return map(int, input().split())
    
def si():
        return input()
    
    a, b, c, d = nis()
    
    if a > b:
        print('First')
    else:
        print('Second')