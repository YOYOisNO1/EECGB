    # Idea is to find first and last indices of all doors
    # It will be time when door opens and time when door closes and guardian can leave
    
def main():
        opened = {}
        closed = {}
    
        n, k = map(int, input().split())
        seq = input()
    
        for i, way in enumerate(seq):
            if way not in opened:
                opened[way] = i
            closed[way] = i # Door can be closed after 1 person in
    
        for i, way in enumerate(seq):
            open_ith_door = opened[way] == i
            if open_ith_door:
                k -= 1
                no_guardians = k < 0
                if no_guardians:
                    print("YES")
                    return
    
            close_ith_door = closed[way] == i
            if close_ith_door:
                k += 1
            else:
                continue
    
        print("NO")
        return
    
    main()