    __author__ = 'Darren'
    
    
def solve():
    
    def calc(lower, upper, record, eq, eq_i):
            if lower > upper:
                return 1
            key = lower, eq, eq_i
            if key in record:
                return record[key]
    
            t = 0
            for x in (['0', '1'] if result[lower] == '?' else [result[lower]]):
                temp = None
                if lower == upper:
                    temp = [x]
                elif result[upper] == '?':
                    temp = ['0', '1']
                else:
                    temp = [result[upper]]
                for y in temp:
                    if not ((eq and x > y) or (eq_i and x == y == '1')):
                        t += calc(lower+1, upper-1, record, eq and x == y,
                                  eq_i and x != y)
            record[key] = t
            return t
    
    
        n, k = map(int, input().split())
        k += 1  # Suppose 00...0 is also valid
        result = ['?'] * n
        for i in range(n):
            result[i] = '0'
            passed = calc(0, n-1, {}, True, True)
            if k > passed:
                k -= passed
                result[i] = '1'
        if result[0] == '0':
            print(''.join(result))
        else:
            print(-1)
    
    
    
    
    
    if __name__ == '__main__':
        solve()