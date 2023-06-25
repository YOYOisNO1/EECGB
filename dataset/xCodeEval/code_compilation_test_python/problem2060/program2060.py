def find_object_idx(cells, symbol):
        for idx, val in enumerate(cells):
            if val == symbol:
                return idx
    
    if __name__ == "__main__":
        num_cells, k = [int(x) for x in input.split()]
        cells = input()
    
        grasshopper_idx = find_object_idx(cells, "G")
        insect_idx = find_object_idx(cells, "T")
        start_index = min(grasshopper_idx, insect_idx)
        target_index = max(grasshopper_idx, insect_idx)
        while start_index <= target_index:
            if start_index == target_index:
                print("YES")
                return
            elif start_index == "#":
                print("NO")
                return
            start_index += k
        print("NO")
        