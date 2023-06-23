    
    
    import sys
    
    cache = {}
    
def max_possible(pie_slices, current_slice, pre_sums):
    
        if current_slice in cache:
            return cache[current_slice]
    
        if len(pie_slices) - 1 == current_slice:
            return pie_slices[current_slice]
    
        opp = pie_slices[current_slice]
        for cs in range(current_slice + 1, len(pie_slices)):
            c1 = max_possible(pie_slices, cs, pre_sums)
            if opp > c1:
                return opp
    
            opp += pie_slices[cs]
    
        return pie_slices[current_slice] + pre_sums[current_slice + 1] - max_possible(pie_slices, current_slice + 1, pre_sums)
    
def main():
        n = int(sys.stdin.readline().strip())
    
        pie_slices = [int(tok) for tok in sys.stdin.readline().strip().split()]
    
        pre_sums = [sum(pie_slices[i:]) for i in range(len(pie_slices))]
    
        b = max_possible(pie_slices, 0, pre_sums)
        print(sum(pie_slices) - b, b)
    
    
    
    
    
    
    
    
    if __name__ == '__main__':
        main()