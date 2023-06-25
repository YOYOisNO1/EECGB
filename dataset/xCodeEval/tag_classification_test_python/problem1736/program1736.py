def list_from_input():
        return list(map(int, input().split()))
    
    
def main():
        l, r, x, y, k = list_from_input()
    
        cost_range = range(x, y+1)
        exp_range = range(l, r+1)
    
        for cost in cost_range:
            needed_exp = k * cost
            potion_found = (int(needed_exp) == needed_exp and
                            needed_exp in exp_range)
            if potion_found:
                print("YES")
                return
    
        print("NO")
        return
    
    main()