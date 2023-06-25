def f(array_size, bits_n, mod):
        row_states_n = pow(2, array_size, mod)
        row_states_n_half = pow(2, array_size-1, mod)
        final_bits_n = bits_n; del bits_n
        curr_result = 1 % mod
        possible_states_accumulated = 1 % mod
        for curr_bits_n in range(1, final_bits_n+1):
            prev_result = curr_result
            curr_result = 0
            if array_size % 2 == 0:
                curr_result += possible_states_accumulated
            curr_result += prev_result * _find_children_n(array_size, curr_bits_n, mod, row_states_n_half)
            curr_result %= mod
            possible_states_accumulated *= row_states_n
            possible_states_accumulated %= mod
        return curr_result
    
    
def _find_children_n(array_size, bits_n, mod, row_states_n_half):
        children_n = row_states_n_half
        if array_size % 2 == 0:
            children_n -= 1
        else:
            children_n += 1
        return children_n
    
    
def _main():
        tests_n = int(input())
        for i_test in range(tests_n):
            n, k = map(int, input().split())
            result = f(n, k, 10**9 + 7)
            print(result)
    
    
    if __name__ == "__main__":
        _main()