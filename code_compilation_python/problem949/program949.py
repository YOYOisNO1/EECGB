    import resource as _resource
    import sys as _sys
    
    
def _main():
        _sys.setrecursionlimit(2**31-1)
        _resource.setrlimit(_resource.RLIMIT_STACK, (2**29, -1)))
        tests_n = int(input())
        for i_test in range(tests_n):
            n, k = map(int, input().split())
            result = f(n, k, 10**9 + 7)
            print(result)
    
    
    _f_cache = dict()
def f(array_size, bits_n, mod):
        if bits_n == 0:
            return 1 % mod
        key = (array_size, bits_n, mod)
        if key in _f_cache:
            return _f_cache[key]
        result = 0
        can_reach_and_1_xor_0 = array_size % 2 == 0
        if can_reach_and_1_xor_0:
            result += pow(2, array_size*(bits_n-1), mod)
        else:
            result += f(array_size, bits_n-1, mod)
        and_0_xor_0_n = pow(2, array_size-1, mod)
        if can_reach_and_1_xor_0:
            and_0_xor_0_n -= 1
        result += and_0_xor_0_n * f(array_size, bits_n-1, mod)
        result %= mod
        _f_cache[key] = result
        return result
    
    
    if __name__ == "__main__":
        _main()