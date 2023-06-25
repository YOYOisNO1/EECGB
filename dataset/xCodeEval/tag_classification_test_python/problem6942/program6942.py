    from math import inf as __inf, isinf as __isinf
    
    
def how_many_operations_need(seq):
        seq = list(seq)
        if any(seq[i] > seq[i+1] for i in range(len(seq) - 1)):
            return 0
        max_bits_indices = tuple(map(__get_max_bit_index, seq))
        for i in range(len(max_bits_indices) - 2):
            if max_bits_indices[i] == max_bits_indices[i+1] == max_bits_indices[i+2]:
                return 1
        
        if any((seq[i] ^ seq[i+1]) < seq[i-1] for i in range(1, len(seq) - 1)):
            return 1
        
        result = __inf
        curr_cost = 0
        while len(seq) >= 3:
            x1, x2 = seq[-2], seq[-1]
            if __get_max_bit_index(x1) != __get_max_bit_index(x2):
                seq.pop()
                curr_cost = 0
            else:
                xor_with_prev = x1
                for i in range(64):  # TODO: buggy
                    if len(seq)-3-i < 0:
                        break
                    xor_with_prev ^= seq[-3-i]
                    if xor_with_prev > x2:
                        result = min(result, curr_cost + (i + 1))
                        break
                seq.pop()
                seq[-1] = x1 ^ x2
                curr_cost += 1
                if seq[-2] > seq[-1]:
                    result = min(result, curr_cost)
                    seq.pop()
                    curr_cost = 0
                elif len(seq) >= 3 and (
                        __get_max_bit_index(seq[-3])
                        ==
                        __get_max_bit_index(seq[-2])
                        ==
                        __get_max_bit_index(seq[-1])
                ):
                    result = min(result, curr_cost + 1)
                    seq.pop()
                    curr_cost = 0
        
        if __isinf(result):
            raise ValueError
        return result
    
    
def __get_max_bit_index(x):
        i = -1
        while x:
            x >>= 1
            i += 1
        return i
    
    
def __main():
        __read_ints()  # skip n
        try:
            result = how_many_operations_need(__read_ints())
        except ValueError:
            print(-1)
        else:
            print(result)
    
    
def __read_ints():
        return map(int, input().split())
    
    
    if __name__ == "__main__":
        __main()