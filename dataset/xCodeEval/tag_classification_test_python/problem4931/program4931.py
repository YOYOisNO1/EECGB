    import sys
    import bisect
    
def gen(start, end, ar, distinct_values, value, mod):
        if start == end:
    	distinct_values.add(value)
    	return
        
        gen(start + 1, end, ar, distinct_values, value, mod)
        gen(start + 1, end, ar, distinct_values, (value + ar[start])%mod, mod)
    
def main():
        n, m = map(int, input().split())
        ar = map(int, input().split())
        
        first, second = set(), set()
        gen(0, n//2, ar, first, 0, m)
        gen(n//2, n, ar, second, 0, m)
        
        first = sorted(first)
        second = sorted(second)
        print(max(x) + second[bisect.bisect_left(second, m - x) - 1] for x in first)
        
        
        
    if __name__ == '__main__':
        main() 
        