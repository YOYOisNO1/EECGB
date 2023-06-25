    from itertools import accumulate as __accumulate
    from math import inf as __inf, isinf as __isinf
    
    
def how_many_operations_need(seq):
        seq = list(seq)
        if any(seq[i] > seq[i+1] for i in range(len(seq) - 1)):
            return 0
        max_bits_indices = tuple(map(__get_max_bit_index, seq))
        for i in range(len(max_bits_indices) - 2):
            if max_bits_indices[i] == max_bits_indices[i+1] == max_bits_indices[i+2]:
                return 1
        
        prefix_xors = [0, *__accumulate(seq, int.__xor__)]
        
        result = +__inf
        for l in range(len(seq)-1):
            for r in range(l+1, len(seq)):
                left_value = seq[l-1] if l-1 >= 0 else -__inf
                right_value = seq[r+1] if r+1 < len(seq) else +__inf
                if not (left_value <= prefix_xors[r+1] ^ prefix_xors[l] <= right_value):
                    result = min(result, r - l)
        
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